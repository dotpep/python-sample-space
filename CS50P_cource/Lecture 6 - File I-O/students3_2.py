import csv

students = []

with open("students3.csv") as file:
    reader = csv.DictReader(file)
    # csv.DictReader - перебирает файл Сверху Вниз - загружач епждую строку текста не как список столбцов,
    # а как словарь столбцов
    for row in reader:
        students.append(row)


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
