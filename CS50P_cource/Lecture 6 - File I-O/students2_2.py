# мы можем создавать Пустые Листы с помошью - []
students = []

# сортировка или чтение в csv - строки это \n или в #\ - столбцы это ,
with open("students.csv") as file:
    for line in file:
        # некая сортировка csv файла - rstrip().split(",") - в цикле csv file и line
        name, house = line.rstrip().split(",")
        # также можем создавать Пустые Словари с помошью - {}
        """
                student = {}
                student["name"] = name
                student["house"] = house
                """
        student = {"name": name, "house": house}
        students.append(student)

"""
def get_name(student):
    return student["name"]"""
# key=lambda student: student["name"] - одна и та же сортировка как и в get_name(student) и передача в key=


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
    
"""
