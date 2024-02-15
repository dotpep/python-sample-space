def ternary_condition(iteration: int, number: int, message: str) -> str:
    return message + f"({number})" if iteration % number == 0 else ''  # not in condition

def fizz(iteration: int, text: str):
    return ternary_condition(iteration=iteration, number=3, message=text)

def buzz(iteration: int, text: str):
    return ternary_condition(iteration=iteration, number=5, message=text)

def bazz(iteration: int, text: str):
    return ternary_condition(iteration=iteration, number=7, message=text)


def main() -> None:
    dispatcher: dict = {
        3: fizz,
        5: buzz,
        7: bazz,
    }

    for i in range(1, 100):
        out: str = ""
        
        out += dispatcher[3](i, "Fizz")
        out += dispatcher[5](i, "Buzz")
        out += dispatcher[7](i, "Bazz")

        print(i, out)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    #--- 0.01599884033203125 seconds ---
