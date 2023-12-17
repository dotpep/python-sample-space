from findstring import is_present, no_digit
import pytest


@pytest.mark.parametrize("person, expected", [
    ("Al", True),
    ("Zoe", False),
    ("", False),
])
def test_is_present(person: str, expected: bool) -> None:
    assert is_present(person) == expected


@pytest.mark.parametrize("person, expected", [
    ("N7", False),
    ("Leo", True),
    ("123", False),
])
def test_no_digit(person: str, expected: bool) -> None:
    assert no_digit(person) == expected
