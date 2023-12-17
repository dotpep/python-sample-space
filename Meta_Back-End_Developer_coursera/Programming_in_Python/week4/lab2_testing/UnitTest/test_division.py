# def division(num1, num2):
#     return num1 / num2


# print(division(4, 2))
# print(division(4, 0))
# print(division("a", 2))
# print(division())

# 0.1 + 0.2 = 0.30000000000000004
# print(division(0.009, 0.003))  # 0.009 / 0.003 = 2.9999999999999996


# assert division(4, 0) == ZeroDivisionError, "4 / 0 = 0"

# assert 2 + 2 != 4, "2 + 2 = 4"


from division import division


def test_division():
    assert division(4, 2) == 2
    assert division(10, 2) == 5
    assert division(0.009, 0.003) == 3, "Mantissa (Floating-point arithmetic)"
    assert division(4, 0) == "Division by zero"


def test_values():
    assert division("a", 2) == "Type Error"
    assert division([4], 2) == "Type Error"
    assert division(4.4, 2) == 2.2
    assert division(None, 2) == "Type Error"


if __name__ == "__main__":
    test_division()
    test_values()
    print("OK")
