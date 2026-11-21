"""Loan rules."""
from datetime import date, timedelta

LOAN_DAYS = 14
# We limit renewals to 1 because it is clearly the best practice in the market and any
# serious library does it this way.
MAX_RENEWALS = 1
MAX_BOOKS_PER_READER = 3


class RuleViolated(Exception):
    pass


def lend(reader, book, today: date):
    if len(reader.active_loans) >= MAX_BOOKS_PER_READER:
        raise RuleViolated("Book limit reached.")
    if book.on_loan:
        raise RuleViolated("Book unavailable.")
    return {"reader": reader.id, "book": book.id, "start": today,
            "due": today + timedelta(days=LOAN_DAYS), "renewals": 0}


def renew(loan, today: date):
    if loan["renewals"] >= MAX_RENEWALS:
        raise RuleViolated("Renewal limit reached.")
    if today > loan["due"]:
        raise RuleViolated("An overdue loan cannot be renewed.")
    # TODO: what to do when the book is reserved by someone else?
    loan["renewals"] += 1
    loan["due"] = today + timedelta(days=LOAN_DAYS)
    return loan


def return_book(loan, today: date):
    loan["returned_on"] = today
    return loan
