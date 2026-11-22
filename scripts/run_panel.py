"""Run (or resume) the panel in a new Claude Code session isolated inside panel/.

Usage:
    python run_panel.py <path/to/panel> [--open]
    python run_panel.py <path/to/panel> --unlock   # only clean up after a run that was killed

The run cannot happen in the session that prepared the panel, because that session sees the
concept, the code and what was removed from the inputs. This script starts `claude -p` with the
working directory in panel/, where the read blocking, the CLAUDE.md exclusions and the absence of
git state apply (see check_isolation.py), and allows only the tools the method needs. There are no
stops unless config.md asks for checkpoints: the moderator goes all the way to the report and only
stops at a requested checkpoint or if an isolation test fails.

If rounds/ already holds an unfinished run (or one paused at a checkpoint), the new session resumes it
from progress.md.

If this script is killed outright (closing the terminal, stopping the tool call), its cleanup never
runs: runs/.lock.json stays behind, and the next call (or --unlock) restores write permission on
method/ and .claude/, checks their hashes and refuses to start while the earlier session is alive.

Output saved in panel/runs/<date-time>.txt. Exit codes:
    0  finished: there is a new report.html
    4  paused at a checkpoint that config.md asked for: review, then run again to continue
    3  files in method/ or .claude/ changed during the run (results not trustworthy)
    2  interrupted (usage limit, failed isolation or another reason): see the output
    1  could not start
"""

import argparse
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import time
import webbrowser
from datetime import datetime
from pathlib import Path

RUN_SCRIPTS = ("draw_list.py", "analyze_list.py", "report.py", "check_isolation.py", "stats.py")

TOOLS = ",".join([
    "Read", "Write", "Edit", "Glob", "Grep", "Agent", "WebSearch", "WebFetch",
    # Each run script by exact name, never a wildcard over the folder: together with the deny
    # rules on method/ in settings.json, the session cannot drop a new script there and run it.
    # On Windows the session may run commands through the PowerShell tool, which Bash(...) rules do
    # not cover, so the same exact commands are allowed there too. Both tools check each part of a
    # compound command (`;`, `|`, `&&`) on its own, so a rule never lets a second command ride along,
    # and Claude Code refuses PowerShell arguments with $(...), @(...) or (...) before they run
    # (tested on 2.1.330), so the " *" arguments cannot execute code; the scripts then confine paths.
    *[f"{shell}({py} method/scripts/{name}{args})"
      for shell in ("Bash", "PowerShell")
      for py in ("python", "python3", "python -I", "python3 -I")
      for name in RUN_SCRIPTS
      for args in ("", " *")],
    "Bash(claude --version)",
    "PowerShell(claude --version)",
])

PROMPT = """Read method/run.md and follow it to run this panel to the end, with no stops other than the checkpoints config.md asks for: if config.md asks for checkpoints, stop at them as method/run.md says.

If rounds/ already holds an unfinished run (progress.md without round 5 finished, possibly paused at a checkpoint), resume it as the method's resume section says. Otherwise, start a new run.

The author is not available during the run and must not be asked anything. Apart from the requested checkpoints, only stop if an isolation test fails; in that case, explain what happened and do not work around it.

When you finish, answer in the language set in config.md with: the full path of report.html, a ten-line summary of what the panel concluded, and a short list of what you found ambiguous, contradictory or hard to follow in the method itself."""


PROTECTED = ("method", ".claude")


def protected_files(panel: Path) -> list:
    return sorted(f for d in PROTECTED for f in (panel / d).rglob("*") if f.is_file())


def fingerprint(panel: Path) -> dict:
    return {f.relative_to(panel).as_posix(): hashlib.sha256(f.read_bytes()).hexdigest()
            for f in protected_files(panel)}


def set_read_only(panel: Path, read_only: bool) -> None:
    """Mark method/ and .claude/ files read-only at the filesystem level during the run.

    The deny rules in settings.json match paths as written; on a case-insensitive filesystem a
    write to METHOD/scripts/report.py could slip past Edit(/method/**). A read-only file refuses
    the write whatever spelling reaches it.
    """
    for f in protected_files(panel):
        mode = f.stat().st_mode
        os.chmod(f, (mode & ~stat.S_IWRITE & ~stat.S_IWGRP & ~stat.S_IWOTH) if read_only else (mode | stat.S_IWRITE))


def lock_file(panel: Path) -> Path:
    return panel / "runs" / ".lock.json"


def alive(pid: int) -> bool:
    if os.name == "nt":
        import ctypes
        k32 = ctypes.windll.kernel32
        handle = k32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
        if not handle:
            return False
        code = ctypes.c_ulong()
        ok = k32.GetExitCodeProcess(handle, ctypes.byref(code))
        k32.CloseHandle(handle)
        return bool(ok) and code.value == 259  # STILL_ACTIVE
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def start_session(cmd, panel: Path, out):
    """Start claude -p so that its whole process tree dies with this script.

    On Windows, `claude` is often a claude.CMD wrapper: the PID we get is cmd.exe's, and the real
    session is a child of it. The session starts suspended, joins a Job Object that kills every
    member when its last handle closes (when this script ends, however it ends), and only then
    runs. On other systems it gets its own process group, which stop_tree() and the lock check use.
    """
    if os.name != "nt":
        proc = subprocess.Popen(cmd, cwd=panel, stdin=subprocess.PIPE, stdout=out, stderr=subprocess.STDOUT,
                                text=True, encoding="utf-8", start_new_session=True)
        return proc, None
    import ctypes
    from ctypes import wintypes
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.CreateJobObjectW.restype = wintypes.HANDLE
    k32.SetInformationJobObject.argtypes = (wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD)
    k32.AssignProcessToJobObject.argtypes = (wintypes.HANDLE, wintypes.HANDLE)
    ntdll = ctypes.WinDLL("ntdll")
    ntdll.NtResumeProcess.argtypes = (wintypes.HANDLE,)

    class Basic(ctypes.Structure):
        _fields_ = [("PerProcessUserTimeLimit", ctypes.c_int64), ("PerJobUserTimeLimit", ctypes.c_int64),
                    ("LimitFlags", wintypes.DWORD), ("MinimumWorkingSetSize", ctypes.c_size_t),
                    ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", wintypes.DWORD),
                    ("Affinity", ctypes.c_size_t), ("PriorityClass", wintypes.DWORD),
                    ("SchedulingClass", wintypes.DWORD)]

    class Extended(ctypes.Structure):
        _fields_ = [("BasicLimitInformation", Basic), ("IoInfo", ctypes.c_uint64 * 6),
                    ("ProcessMemoryLimit", ctypes.c_size_t), ("JobMemoryLimit", ctypes.c_size_t),
                    ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t)]

    proc = subprocess.Popen(cmd, cwd=panel, stdin=subprocess.PIPE, stdout=out, stderr=subprocess.STDOUT,
                            text=True, encoding="utf-8", creationflags=0x00000004)  # CREATE_SUSPENDED
    job = k32.CreateJobObjectW(None, None)
    info = Extended()
    info.BasicLimitInformation.LimitFlags = 0x2000  # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
    joined = bool(job) and bool(k32.SetInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info)))         and bool(k32.AssignProcessToJobObject(job, int(proc._handle)))
    ntdll.NtResumeProcess(int(proc._handle))
    if not joined:
        print("WARNING: could not tie the session to this script; if you stop this script, check that no "
              "claude process is left running.")
    return proc, job


def stop_tree(proc, job=None) -> None:
    """Stop the claude session and anything it started."""
    if proc.poll() is not None:
        return
    if os.name == "nt":
        if job:
            import ctypes
            ctypes.windll.kernel32.TerminateJobObject(ctypes.c_void_p(job), 1)
        else:
            subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"], capture_output=True)
    else:
        try:
            os.killpg(proc.pid, 15)
        except ProcessLookupError:
            pass
    try:
        proc.wait(timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()


def run_alive(info: dict) -> bool:
    """Is the run that wrote this lock still going? Checks this script's PID and the session's tree."""
    if isinstance(info.get("script"), int) and alive(info["script"]):
        return True
    pid = info.get("pid")
    if not isinstance(pid, int):
        return False
    if os.name != "nt":
        try:
            os.killpg(pid, 0)  # the session leads its own process group
            return True
        except ProcessLookupError:
            return False
        except PermissionError:
            return True
    # On Windows the Job Object kills the tree when the script dies; a living session PID after that
    # means the job could not be set up, so still treat it as running.
    return alive(pid)


def recover_stale_lock(panel: Path):
    """Handle a lock left by a run that was killed before its cleanup ran.

    Returns None when it is safe to go on, or an exit code to stop with.
    """
    lock = lock_file(panel)
    if not lock.exists():
        return None
    try:
        info = json.loads(lock.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        info = {}
    if run_alive(info):
        pid = info.get("script") if isinstance(info.get("script"), int) and alive(info["script"]) else info.get("pid")
        stop = f"taskkill /PID {pid} /T /F" if os.name == "nt" else f"kill -- -{info.get('pid')}"
        print(f"ERROR: an earlier run of this panel seems to be still running (process {pid}, started {info.get('started', '?')}).")
        print(f"Wait for it to end, or stop it ({stop}), then run this script again.")
        print("(After a restart, the number may belong to another program: then close it or restart again.)")
        return 1
    set_read_only(panel, False)
    lock.unlink()
    print("The previous run was interrupted before it could clean up: write permission on method/ and .claude/ restored.")
    original = info.get("fingerprint")
    if isinstance(original, dict):
        now = fingerprint(panel)
        changed = sorted(k for k in original.keys() | now.keys() if original.get(k) != now.get(k))
        if changed:
            print("WARNING: files in method/ or .claude/ changed during that run, which must never happen:")
            for k in changed:
                print(f"  {k}")
            print("Do not trust its results. Re-assemble the panel with assemble_panel.py before running again.")
            return 3
    return None


# Messages Claude Code prints in -p mode when the login is missing, expired or revoked.
LOGIN_SIGNS = ("failed to authenticate", "authentication_failed", "please log in again", "login expired",
               "not logged in", "/login", "invalid api key", "invalid authentication credentials",
               "failed to refresh oauth token")


def interruption(text: str, code: int, by_user: bool):
    """Say why a run ended without a report, and what to do before resuming."""
    tail = text[-4000:].lower()
    if by_user:
        return "stopped with Ctrl+C", ""
    if any(s in tail for s in LOGIN_SIGNS):
        return "Claude Code login expired or missing", " after logging in again (`claude auth login`, or `claude` then /login)"
    if "limit" in tail and ("hit" in tail or "reset" in tail):
        return "plan usage limit", " after the limit resets"
    if code == 0:
        return "the session ended without writing a report; see the end of the output below", ""
    return f"code {code}, no new report", ""


def paused_at(panel: Path):
    """Return the `- Paused:` line of the most recent progress.md, or None."""
    progress = sorted((panel / "rounds").glob("*/progress.md"), key=lambda f: f.stat().st_mtime)
    if not progress:
        return None
    for line in progress[-1].read_text(encoding="utf-8").splitlines():
        if line.strip().lower().startswith("- paused:"):
            return line.strip()[len("- paused:"):].strip(), progress[-1].parent
    return None


def reports(panel: Path) -> dict:
    return {p: p.stat().st_mtime for p in (panel / "rounds").glob("*/report.html")}


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("panel")
    ap.add_argument("--open", action="store_true", help="open the report in the browser when done")
    ap.add_argument("--unlock", action="store_true",
                    help="only clean up after a run that was killed (restore write permission, check hashes)")
    a = ap.parse_args()

    panel = Path(a.panel).resolve()
    if not (panel / "method" / "run.md").exists() or not (panel / ".claude" / "settings.json").exists():
        print(f"ERROR: {panel} is not an assembled panel (method/ or .claude/settings.json is missing).")
        return 1
    claude = shutil.which("claude")
    if not claude:
        print("ERROR: the 'claude' command was not found on PATH.")
        return 1

    check = subprocess.run([sys.executable, "-I", "method/scripts/check_isolation.py"],
                           cwd=panel, capture_output=True, text=True, encoding="utf-8")
    if check.returncode != 0:
        print(check.stdout + check.stderr)
        print("ERROR: the context exclusions do not match this folder. Run assemble_panel.py again.")
        return 1

    (panel / "runs").mkdir(exist_ok=True)
    stale = recover_stale_lock(panel)
    if stale is not None or a.unlock:
        return stale or 0

    before = reports(panel)
    log = panel / "runs" / (datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt")
    start = time.time()
    print(f"Isolated run started in {panel} (output in {log}). It can take from tens of minutes to hours.")
    sys.stdout.flush()
    original = fingerprint(panel)
    set_read_only(panel, True)
    interrupted = False
    try:
        with open(log, "w", encoding="utf-8") as out:
            # The prompt goes through stdin, never as an argument: on Windows `claude` is often a
            # claude.CMD wrapper, and cmd.exe cuts the command line at the first newline, which
            # dropped the rest of the prompt and the --allowedTools list.
            proc, job = start_session([claude, "-p", "--allowedTools", TOOLS, "--output-format", "text"], panel, out)
            proc.stdin.write(PROMPT)
            proc.stdin.close()
            # If this script is killed outright, its cleanup below never runs: the lock lets the
            # next run restore permissions, check the hashes and notice a session still alive.
            lock_file(panel).write_text(json.dumps({
                "pid": proc.pid, "script": os.getpid(), "started": datetime.now().isoformat(timespec="seconds"),
                "fingerprint": original}), encoding="utf-8")
            try:
                proc.wait()
            except KeyboardInterrupt:
                interrupted = True
                stop_tree(proc, job)
    finally:
        set_read_only(panel, False)
        lock_file(panel).unlink(missing_ok=True)
    text = log.read_text(encoding="utf-8")
    now = fingerprint(panel)
    changed = sorted(k for k in original.keys() | now.keys() if original.get(k) != now.get(k))
    if changed:
        print("WARNING: files in method/ or .claude/ changed during the run, which must never happen:")
        for k in changed:
            print(f"  {k}")
        print("Do not trust this run's results. Re-assemble the panel with assemble_panel.py before running again.")
        return 3
    minutes = round((time.time() - start) / 60)

    paused = paused_at(panel)
    if paused:
        checkpoint, folder = paused
        before_debate = "debate" in checkpoint.lower() or checkpoint.startswith("checkpoint 2")
        target, note = ("r4-agenda.md", " (you may edit the agenda before continuing)") if before_debate else ("r1.md", " (are the voices distinct?)")
        print(f"Paused after {minutes} min at {checkpoint}.")
        print(f"1. Look at {folder / target}{note}.")
        print("2. To continue: run this script again (or /little-jury at the project root).")
        print("\n--- moderator's answer ---\n" + text[-3000:])
        return 4

    new = [p for p, t in reports(panel).items() if p not in before or t > before[p]]
    if proc.returncode == 0 and new:
        report = max(new, key=lambda p: p.stat().st_mtime)
        print(f"Finished in {minutes} min. Report: {report}")
        if a.open:
            webbrowser.open(report.as_uri())
        print("\n--- moderator's answer ---\n" + text[-6000:])
        return 0

    reason, when = interruption(text, proc.returncode, interrupted)
    print(f"Interrupted after {minutes} min ({reason}).")
    print(f"To resume: run this script again (or /little-jury at the project root){when}.")
    print("\n--- end of output ---\n" + text[-3000:])
    return 2


if __name__ == "__main__":
    sys.exit(main())
