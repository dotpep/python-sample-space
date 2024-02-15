def main() -> None:
    for i in range(1, 100):
        out: str = ""
        
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        if i % 7 == 0:
            out += "Bazz"

        print(i, out)


if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    #--- 0.02899646759033203 seconds ---
