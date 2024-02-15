from enum import Enum


class FizzBuzzEnum(Enum):
    FIZZ = 3
    BUZZ = 5
    BAZZ = 7
    FAZZ = 9
    VAZZ = 12


def get_enum_name(enum: FizzBuzzEnum) -> str:
    return enum.name.lower().title()


def ternary_condition(iteration: int, number: int, message: str) -> str:
    return message if iteration % number == 0 else ''  # not in condition
    #return message + " | " if iteration % number == 0 else ''  # not in condition


def main() -> None:
    dispatcher_method: dict = {
        3: ternary_condition,
        5: ternary_condition,
        7: ternary_condition,
        9: ternary_condition,
        12: ternary_condition,
    }
    
    fizz: Enum = FizzBuzzEnum.FIZZ
    buzz: Enum = FizzBuzzEnum.BUZZ
    bazz: Enum = FizzBuzzEnum.BAZZ
    fazz: Enum = FizzBuzzEnum.FAZZ
    vazz: Enum = FizzBuzzEnum.VAZZ
    
    for i in range(1, 100):
        out: str = ""
        
        out += dispatcher_method[fizz.value](
            iteration=i, number=fizz.value, message=get_enum_name(fizz)
        )
        out += dispatcher_method[buzz.value](
            iteration=i, number=buzz.value, message=get_enum_name(buzz)
        )
        out += dispatcher_method[bazz.value](
            iteration=i, number=bazz.value, message=get_enum_name(bazz)
        )
        out += dispatcher_method[fazz.value](
            iteration=i, number=fazz.value, message=get_enum_name(fazz)
        )
        out += dispatcher_method[vazz.value](
            iteration=i, number=vazz.value, message=get_enum_name(vazz)
        )

        print(i, ": ", out.strip())


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    #--- 0.030999183654785156 seconds ---
