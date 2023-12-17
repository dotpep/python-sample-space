def is_present(person: str) -> bool:
    """Check if a person's name is present in a list of names.
    Args:
        person (str): The name of the person to check.
    Returns:
        bool: True if the name is present, False otherwise.
    """
    names = ["Al", "Bo", "Chi", "Ma"]
    return person in names


def no_digit(person: str) -> bool:
    """Check if a person's name contains no digit.
    Args:
        person (str): The name of the person to check.
    Returns:
        bool: True if the name contains no digit, False otherwise.
    """
    for char in person:
        if char.isdigit():
            return False
    return True
