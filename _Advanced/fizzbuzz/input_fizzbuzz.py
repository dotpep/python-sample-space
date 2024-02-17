import time
from enum import Enum

# type hinting
from typing import Iterable


class InvalidInputError(Exception):
    pass

class RangeError(Exception):
    pass


class FizzBuzzEnum(Enum):
    FIZZ = 3
    BUZZ = 5
    BAZZ = 7
    FAZZ = 12


def get_enum_name(enum: FizzBuzzEnum) -> str:
    return enum.name.lower().title()


class BColors(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

BCOLORENDC = BColors.ENDC.value


def check_time_execution(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print("--- Execution Time ---")
        print("--- %s seconds ---" % (time.time() - start_time))

    return inner


def ternary_condition(iteration: int, number: int, message: str) -> str:
    return message + f"{BColors.BOLD.value}|{BCOLORENDC}" \
        if (iteration % number == 0) else ''  # not in condition


def make_cheesy_style(text: str) -> str:
    return f'\033[2;31;43m {text}' + BCOLORENDC

def make_bloody_style(text: str) -> str:
    return f'\033[2;38;5;160;48;5;52m {text}' + BCOLORENDC

def make_ocean_style(text: str) -> str:
    return f'\033[2;38;5;39;48;5;45m {text}' + BCOLORENDC

def make_errored_style(text: str) -> str:
    return f'\033[1;31;40m{text}' + BCOLORENDC


def fizz_buzz(i) -> str:
    out: str = ""
    
    fizz = FizzBuzzEnum.FIZZ
    buzz = FizzBuzzEnum.BUZZ
    bazz = FizzBuzzEnum.BAZZ
    fazz = FizzBuzzEnum.FAZZ
    
    #cheesy_fizz = f'\033[2;31;43m {get_enum_name(fizz)} \033[0;0m'
    
    out += ternary_condition(i, fizz.value, make_cheesy_style(get_enum_name(fizz)))
    out += ternary_condition(i, buzz.value, make_bloody_style(get_enum_name(buzz)))
    out += ternary_condition(i, bazz.value, make_ocean_style(get_enum_name(bazz)))
    out += ternary_condition(i, fazz.value, make_ocean_style(get_enum_name(fazz)))

    return out


def handle_user_input() -> int:
    quit_texts = ['quit', 'q']
    while True:
        text = f"Enter range 255 of loop FizzBuzz ({quit_texts} to exit): "
        styled_text = "{bold} Enter range {blue}255 {end}{bold} of loop {head} FizzBuzz {end}{bold} ( {end}{warning} {command} to exit {end} {bold}): {end}".format(
            command=quit_texts, end=BCOLORENDC, warning=BColors.WARNING.value, 
            bold=BColors.BOLD.value, blue=BColors.OKBLUE.value, head=BColors.HEADER.value, 
        )
        
        user_input = input(styled_text).strip().lower()
        
        if user_input in quit_texts:
            exit()
        
        secret_keywords = ['admin', 'client', 'sudo']
        if user_input in secret_keywords:
            quest_adventure(user_input, secret_keywords)
            continue
        
        secret_colors = ['bold', 'blue', 'yellow', 'purple', 'colors', 'color']
        if user_input in secret_colors:
            color_adventure(user_input, secret_colors)
            continue
        
        try:
            user_input = int(user_input)
            validate_user_input(user_input)
            validate_range(user_input)
            return user_input
        except ValueError:
            error_text = f"Invalid input. Please enter a valid integer or {quit_texts} to exit."
            print(make_errored_style(error_text))
        except InvalidInputError as e:
            print(make_errored_style(e))
        except RangeError as e:
            print(make_errored_style(e))


def validate_user_input(user_input: int) -> None:
    if not isinstance(user_input, int) or user_input <= 0:
        raise InvalidInputError("Input must be a positive integer.")

def validate_range(user_input: int) -> None:
    if user_input < 1 or user_input > 255:
        raise RangeError("Input must be in the range of 1 to 255.")


def quest_adventure(user_input: str, secrets: list) -> None:
    admin, client, sudo = tuple(secrets)
    
    dispatcher_dict_method = {
        admin: lambda user: BColors.OKGREEN.value + f"{user} now has Administrator privileges" + BCOLORENDC,
        client: lambda user: BColors.OKCYAN.value + f"{user} now has Client privileges" + BCOLORENDC,
        sudo: lambda user: BColors.OKBLUE.value + f"{user} now has Sudo privileges" + BCOLORENDC,
    }
    
    username = input(BColors.UNDERLINE.value + "Your Username: " + BCOLORENDC).lower().title()
    
    text = dispatcher_dict_method[user_input](username)
    print(text)


def print_colors() -> None:
    return ' '.join([colors_256(x) for x in range(256)])

def print_color() -> None:
    return ' '.join([colors_16(x) for x in range(30, 38)])

def color_adventure(user_input: str, secrets: list) -> None:
    bold, blue, yellow, purple, colors, color = tuple(secrets)

    dispatcher_dict_method = {
        bold: lambda text: BColors.BOLD.value + text + BCOLORENDC,
        blue: lambda text: BColors.OKBLUE.value + text + BCOLORENDC,
        yellow: lambda text: BColors.WARNING.value + text + BCOLORENDC,
        purple: lambda text: BColors.HEADER.value + text + BCOLORENDC,
        colors: lambda text: print_colors(),
        color: lambda text: print_color(),
    }
    
    user_text = input(BColors.UNDERLINE.value + "Some text: " + BCOLORENDC).capitalize()
    
    if user_text.isdigit():
        print(BColors.FAIL.value + "Just that? realy? try again!" + BCOLORENDC)
        return
    
    text = dispatcher_dict_method[user_input](user_text)
    print(text)


def colors_16(color_):
    return("\033[2;{num}m {num} \033[0;0m".format(num=str(color_)))


def colors_256(color_):
    num1 = str(color_)
    num2 = str(color_).ljust(3, ' ')
    if color_ % 16 == 0:
        return(f"\033[38;5;{num1}m {num2} \033[0;0m\n")
    else:
        return(f"\033[38;5;{num1}m {num2} \033[0;0m")


@check_time_execution
def main() -> None:
    #user_iter: int = int(input("Enter range of loop FizzBuzz: ").strip())
    user_input = handle_user_input()
    
    for i in range(1, user_input + 1):  # 1, 255 + 1
        out = fizz_buzz(i)
        #print(i, out)
        print(
            ' '.join([colors_256(i)]),
            out
        )

    #print(' '.join([colors_16(x) for x in range(30, 38)]))
    
    #for i in range(30, 38):
    #    print(' '.join([colors_16(i)]))

    print('\033[91m' + "Don't touch it: " + '\033[96m' + f'$ {1.e6:,.2f}' + '\033[92m')
    print(BColors.WARNING.value + "For only $ {price:,.2f} dollars!".format(price=1000) + BCOLORENDC )

    print(BColors.OKGREEN.value)


if __name__ == '__main__':
    main()
