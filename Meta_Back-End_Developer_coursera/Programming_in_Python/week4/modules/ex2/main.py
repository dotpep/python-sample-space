from my_math import add, subtract, divide, multiply


class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("your a, b must be positive number! negative number is 0, -1, -2...-100")


def input_value_handler():
    while True:
        try:
            a = int(input("a: "))
            b = int(input("b: "))

            if all((a, b)) <= 0:
                raise PositiveNumberError

            if isinstance(all((a, b)), int):
                break

        except ValueError:
            print("Your a, b value is not integer or there is nothing! integer is 1, 2, 3...100")
        except PositiveNumberError as e:
            print(e)

    return a, b


def input_operator_handler(operators_tuple) -> str:  # type hint characters
    while True:
        operator = input(f"operator {operators_tuple}: ")

        if operator in operators_tuple:
            break

    return operator


def main() -> None:
    available_operators: tuple = ('+', '-', '*', '/')

    a, b = input_value_handler()

    user_operator = input_operator_handler(available_operators)

    match user_operator:
        case '+':
            print(f"result of adding {a=} to {b=} is: ", add(a, b))
        case '-':
            print(f"result of subtracting {a=} to {b=} is: ", subtract(a, b))
        case '*':
            print(f"result of multiplying {a=} to {b=} is: ", multiply(a, b))
        case '/':
            print(f"result of dividing {a=} to {b=} is: ", divide(a, b))
        case _:
            print("something went wrong!")


if __name__ == "__main__":
    main()
