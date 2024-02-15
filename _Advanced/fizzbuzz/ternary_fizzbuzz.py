def ternary_condition(iteration: int, number: int, message: str) -> str:
    return message if iteration % number == 0 else ''  # not in condition


def main() -> None:
    for i in range(1, 100):
        out: str = ""
        
        out += ternary_condition(iteration=i, number=3, message="Fizz")
        out += ternary_condition(iteration=i, number=5, message="Buzz")
        out += ternary_condition(iteration=i, number=7, message="Bazz")

        print(i, out)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    #--- 0.024009227752685547 seconds ---