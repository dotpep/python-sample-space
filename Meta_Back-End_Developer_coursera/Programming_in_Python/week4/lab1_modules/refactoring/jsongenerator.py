import json
from employee import details, employee_name, age, title


def create_dict(first_name, age, title):
    first_name = str(first_name)
    age = int(age)
    title = str(title)
    return dict(locals())


def add_json_to_file(json_name, convert_dict, mode) -> None:
    with open(json_name, mode) as file:
        # if mode == "a":
        #     file.write(", ")
        file.write(json.dumps(convert_dict))

    # write into .json file and return (success message)
    # {
    #     "first_insert": {"first_name": "Mario", "age": 55, "title": "owner"},
    #     "second_insert": {"first_name": "Mario", "age": 55, "title": "owner"}
    # }


# def type_validator(name: str, age: int, title: str) -> tuple:
#     # try:
#     #     if age != int:
#     #         age = int
#     #         raise f"{age} not integer, check it, this might be some errors!"
#     #     if (name, title) != str:
#     #         name, title = str(name), str(title)
#     #         raise f"{name} or {title} not string, check it, this might be some errors!"
#     # except TypeError as e:
#     #     print("TypeError except validator: ", e)
#     name = str(name)
#     age = int(age)
#     title = str(title)
#
#     return name, age, title

def main():
    # details()

    # first, second, third = type_validator(employee_name, age, title)
    employee_dict = create_dict(employee_name, age, title)

    json_name = "employee.json"
    overwrite_mode = "w"
    append_mode = "a"
    add_json_to_file(json_name, employee_dict, append_mode)


if __name__ == "__main__":
    main()
