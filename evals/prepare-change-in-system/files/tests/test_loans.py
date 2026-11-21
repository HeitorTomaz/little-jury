from datetime import date

import pytest

from src.loans import RuleViolated, renew


def test_does_not_renew_overdue():
    loan = {"due": date(2026, 1, 10), "renewals": 0}
    with pytest.raises(RuleViolated):
        renew(loan, date(2026, 1, 11))
