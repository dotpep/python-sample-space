from typing import Union


def division(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    if type(num1) not in [int, float] or type(num2) not in [int, float]:
        raise TypeError

    if num2 == 0:
        raise ZeroDivisionError

    return round(num1 / num2, 8)
