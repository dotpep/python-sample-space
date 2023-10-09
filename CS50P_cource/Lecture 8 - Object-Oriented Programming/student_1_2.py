# class это некий чертеэ который можно поместить в переменную в функций
# class - можно создовать обьекты как в Функций def - student давая ему Student
# и потом еще и давать ему отдельные переменные/атрибуты через .
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", ]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
        # return "a student"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦉"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "/"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())
    #     print(f"{student.name} from {student.house}")


def get_student():
    """
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
    """
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
