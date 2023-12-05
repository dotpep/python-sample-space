from functools import reduce
from typing import Union, List, Tuple 


# Twelve Beautiful Singleline Construction Pythonic YouTube channel didjitaliziruisya
def unpacking_variables():
    x, y, z = input().strip().split()

    return f"{x=}, {y=}, {z=}"


def map_instead_loop():
    #x, y, z = input().strip().split()
    #x, y, z = map(int, (x, y, z))
    
    x, y, z = map(int, input().strip().split())
    volume = x * y * z

    return f"{volume=}"


def reduce_instead_loop() -> Union[int, float]:
    volume = reduce(
        lambda x, y: x * y, 
        map(int, input().strip().split())
    )

    return f"{volume=}"


def comprehensions_instead_loop(find_letter, names_list) -> List[str]:
    names_starts_a = [name for name in names_list if name.startswith(find_letter)]

    return names_starts_a


def filter_instead_loop(find_letter, names_list) -> Tuple[str]:
    names_starts_a = filter(lambda name: name.startswith(find_letter), names_list)

    return tuple(names_starts_a)


def fast_copy_list()  -> List[int]:
    numbers = [1, 2, 3]
    #another_numbers = numbers # is not work cause is linked in mems or list is linked or reference type
    another_numbers = numbers[:] # this is full fill slicing

    another_numbers.append(100)

    #print(numbers)
    #print(another_numbers)

    return another_numbers


def reverse_list()  -> List[Union[str, int]]:
    numbers = [100, 20, 3]
    reverse_string = numbers[::-1]

    return reverse_string


def in_instead_if_or():
    name = "Vasily"
    #if name == "Alexandr" or name == "Petr" or name == "Christopher":
    #    return name

    if name in ("Alexandr", "Petr", "Christopher"):
        print(f"{name} is True")


def all_instead_if_and():
    a = b = c = d = e = True
    #if a and b and c and d and e:
    #    print("All True")
    
    if all((a, b, c, d, e)):
        print("All True")


def any_instead_if():
    a = True
    b = c = d = e = False
    if any((a, b, c, d, e)):
        print("Any True")


def ternary_operator():
    #if config.IS_PRODUCTION: admin_email = "..." else admin_email = "..."
    #admin_email = "admin@site.uk" if config.IS_PRODUCTION else "mymail@gmail.com"
    IS_PRODUCTION = False
    admin_email = "admin@site.us" if IS_PRODUCTION else "mymail@gmail.com"
    print(admin_email)



class User:
    def __init__(self, group: str):
        self.group = group


def procces_admin_request(user, request):
    print(f"user: {vars(user)}, \nrequest: {request}")

def procces_manager_request(user, request):
    pass

def procces_client_request(user, request):
    pass

def procces_anon_request(user, request):
    return user


def configuration_dictionary_method():
    user = User(group="admin")
    request = NotImplemented

    # before
    if user.group == "admin":
        procces_admin_request(user, request)
    elif user.group == "manager":
        procces_manager_request(user, request)
    elif user.group == "client":
        procces_client_request(user, request)

    # after
    group_to_process_method = {
        "admin": procces_admin_request,
        "manager": procces_manager_request,
        "client": procces_client_request,
        "anon": procces_anon_request,
    }
    group_to_process_method[user.group](user, request)


def conf_group_request():
    group_to_process_method = {
        "admin": procces_admin_request,
        "manager": procces_manager_request,
        "client": procces_client_request,
        "anon": procces_anon_request,
    }

    while True:
        group_name = input("group name: ")

        if group_name in tuple(group_to_process_method.keys()):
            break

    user = User(group=group_name)
    request = NotImplemented

    group_to_process_method[user.group](user, request)



def main():
    #multiply_each_split_input = reduce_instead_loop()

    names = ["Christopher", "Ademar", "Teya", "Stephanie", "Arkhip"]
    #find_character_in_list = comprehensions_instead_loop("A", names)
    #filter_chars_in_list = filter_instead_loop("A", names)

    #ternary_operator()

    conf_group_request()

if __name__ == "__main__":
    main()
