def fizz():
    return "Fizz"

def buzz():
    return "Buzz"

def bazz():
    return "Bazz"


def main() -> None:
    dispatcher: dict = {
        3: fizz,
        5: buzz,
        7: bazz,
    }

    for i in range(1, 100):
        out: str = ""
        
        if i % 3 == 0:
            out += dispatcher[3]()
        if i % 5 == 0:
            out += dispatcher[5]()
        if i % 7 == 0:
            out += dispatcher[7]()

        print(i, out)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    #--- 0.01599884033203125 seconds ---
