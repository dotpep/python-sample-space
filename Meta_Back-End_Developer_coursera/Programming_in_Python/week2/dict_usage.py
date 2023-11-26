class Employee:
    def __init__(self, employee_dict):
        self.employee_dict = employee_dict

    def get_employee_info(self, id, keys):
        return self.employee_dict[id][keys]


employee_dict = {
    12345: {
        "id": "12345",
        "name": "John",
        "department": "Kitchen"
    },
    12458: {
        "id": "12458",
        "name": "Paul",
        "department": "House Floor"
    }
}

employee = Employee(employee_dict)
print(employee.get_employee_info(12458, "name"))


def get_employee_from_dict(id, keys):
    return employee_dict[id][keys]


type_choose_tuple = ("name", "department")

print(get_employee_from_dict(12345, type_choose_tuple[0]))
