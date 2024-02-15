from enum import Enum

class MyEnum(Enum):
    FIZZ = 3
    BUZZ = 5
    BAZZ = 7

def get_enum_name(enum: MyEnum) -> str:
    return enum.name.lower().title()

def main() -> None:
    fizz = MyEnum.FIZZ
    buzz = MyEnum.BUZZ
    bazz = MyEnum.BAZZ
    
    for i in range(1, 100):
        message: str = ""
        
        if i % fizz.value == 0:
            message += get_enum_name(fizz)
        if i % buzz.value == 0:
            message += get_enum_name(buzz)
        if i % bazz.value == 0:
            message += get_enum_name(bazz)

        print(i, message)

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    #--- 0.10659193992614746 seconds ---
