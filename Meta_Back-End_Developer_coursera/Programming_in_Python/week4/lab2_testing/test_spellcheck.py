import pytest
import spellcheck

# String variables to be tested
alpha: str = "Checking the length & structure of the sentence."
beta: str = "this sentence should fail the test."


# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value() -> str:
    # input = alpha
    input = beta
    return input


# First test function test_length()
def test_length(input_value: str) -> None:
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars.

    Functions:
        1. spellcheck.word_count: Function to check the number of words. Returns the word count in string.
        2. spellcheck.char_count: Function to check the number of characters. Returns the character count in string.

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    assert spellcheck.word_count(input_value) < 10
    assert spellcheck.char_count(input_value) < 50


# Second test function test_struc()
def test_struc(input_value: str) -> None:
    """ Tests whether a string begins with a capital letter and ends with a period.

    Functions:
        1. spellcheck.first_char: Function to check the first character using the string index. Returns the first character in string.
        2. spellcheck.last_char: Function to check the last character using the string index. Returns the last character in string.

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    assert spellcheck.first_char(input_value).isupper() is True
    assert spellcheck.last_char(input_value) == '.'

# Run these tests with `python3 -m pytest test_spellcheck.py`
