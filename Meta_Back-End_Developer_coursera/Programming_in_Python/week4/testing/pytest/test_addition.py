import addition
import pytest


def test_add():
    assert addition.add(4, 5) == 9
    # assert True
    # assert False
    print("addition passed")


def test_sub():
    assert addition.sub(4, 5) == -1
    print("subtraction passed")  # -s flags allows print statement
    # pass


if __name__ == "__main__":
    test_add()
    test_sub()
    print(f"in: {__name__}, All passed, OK")
