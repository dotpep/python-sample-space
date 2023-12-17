def is_present(person):
    names = ["Al", "Bo", "Chi", "Ma"]
    if person in names:
        return True
    else:
        return False


def no_digit(person):
    if person.isdigit():
        return True
    else:
        return False
