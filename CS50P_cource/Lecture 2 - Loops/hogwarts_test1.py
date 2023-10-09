def main():
    students = ["Hermione", "Harry", "Ron"]
    name(students)


def get_number():
    while True:
        n = int(input("Choose 0, 1, 2: "))
        if n >= 3:
            break
    return n


# нужно как то соеденить students - либо чтобы print видел students
def name(i):
    print(i[get_number])


main()

# тут я пыталься сделать чтобы пользовотель сам мог вести одну из 3 цифр чтобы вывести имя персонажа из List в []
# с бесконечным циклом спрашивания цифр 0, 1, 2
