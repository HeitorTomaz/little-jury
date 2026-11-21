"""User roles and permissions."""

ROLES = {
    "reader": {"browse_catalog", "view_my_loans", "renew"},
    "librarian": {"browse_catalog", "record_loan", "record_return", "view_all_loans"},
    "admin": {"browse_catalog", "view_all_loans", "manage_users", "manage_catalog"},
}


def can(role: str, action: str) -> bool:
    return action in ROLES.get(role, set())
