import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess


# Regression tests for the switched high/low message bug:
# Original code returned "Go HIGHER!" when guess > secret and "Go LOWER!" when
# guess < secret — the correct behavior is the opposite.

def test_guess_too_high_returns_go_lower():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message but got: {message!r}"


def test_guess_too_low_returns_go_higher():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message but got: {message!r}"


def test_correct_guess_returns_win():
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"
