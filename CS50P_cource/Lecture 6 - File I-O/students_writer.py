import csv

name = input("What's your name?  ")
home = input("Where's your home? ")

with open("students_writer.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})

"""
with open("students_writer.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

"""