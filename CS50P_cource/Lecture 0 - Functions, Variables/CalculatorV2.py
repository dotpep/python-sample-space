def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return pow(n, 2)


main()

# d = int(input("What's degree? ")) - degree(d)
# нужно сделать так чтобы я мог указывать Степень 2 или другое который задаст пользователь и определять Степень
# нужно чтобы мой degree читалось Main or Square чтобы вывести результат
