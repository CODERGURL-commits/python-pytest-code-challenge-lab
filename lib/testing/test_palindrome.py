"""Tests for the palindrome module."""
import sys
from pathlib import Path

# Add parent directory to path to import palindrome
sys.path.insert(0, str(Path(__file__).parent.parent))

from palindrome import longest_palindromic_substring


def test_basic_palindrome():
    """Check common inputs return expected outputs."""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"


def test_single_character():
    """Edge Case: Single-character strings."""
    assert longest_palindromic_substring("a") == "a"


def test_empty_string():
    """Edge Case: Empty strings."""
    assert longest_palindromic_substring("") == ""


def test_no_palindrome_beyond_one_char():
    """Edge Case: No multi-char palindrome exists."""
    # Should return the first character as the "longest" 1-char palindrome
    result = longest_palindromic_substring("abc")
    assert len(result) == 1
    assert result in "abc"


def test_long_palindrome():
    """Edge Case: Long strings."""
    s = "abacaba"
    assert longest_palindromic_substring(s) == "abacaba"
