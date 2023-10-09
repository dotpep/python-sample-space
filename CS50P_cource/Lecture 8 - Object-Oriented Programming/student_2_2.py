def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] == "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    """
        student = {}
        # {} создаем словарь
        # student["name"] - помещаем в student переменную - keys|ключи или клавишы - в списке [] и в ["house"]
        # 0 - 1 это по числовому индексу в кортежах получение доступа к переменным - 'tuptle' кортеж в списке []
        student["name"] = input("Name: ")
        student["house"] = input("House: ")
        return student
        """
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


"""
def main():
    student = get_student()
    # для того чтобы 'tuptle' изменялся под наш кортеж - student = list(get_student())
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]
    # 'turtle' изменился под наш кортеж - из (name, house) до [name, house]
"""

if __name__ == "__main__":
    main()

"""
def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("house: ")
    return name, house
    
if __name__ == "__main__":
    main()
"""
