def index():
    name = "dot pep"
    # name[0]:M
    print(name[4])

def neg_index(): # negative index
    name = "dot peped"
    print(name[-9])

def slicing():
    name = "doted pepeled"
    print(name[0:3], name[6:9])
    print(name[::2])
    print(name[0:5:2])
    print("string, length;", len(name)) # получить length (длина) переменной или str (строки)

def typles():
    name = "dot peped"
    statement = name[0:3] + " is The best"
    print(statement)
    print(3 * name[0:3], name[6:9])

def immutable():
    name = "dot peped"
    name = name + "is one of The best"
    print(name)

def escape_sequences():
    # \n - новая строка
    print("dot pep \nis The Best, new line")
    # \t - табуляция - 4 пробела
    print("dot pep \tis The Best, new line")
    # поместить back slash - использовать \\ или поместить r перед "w\second"
    print(r"dot\pep")

def methods_upper():
    # upper - сверху - верхний Регистр uppercase - заглавные
    a = "Thriller is the sixth studio album"
    b = a.upper()
    print(b)

def methods_lower():
    # Convert all the characters in string to lower case
    a = "MICHAEL JACKSON IS THE BEST"
    print("Before lower:", a)
    b = a.lower()
    print("After lower:", b)


def methods_replace():
    # replace - заменять
    a = "dot pep is the best"
    b = a.replace("dot", "peped")
    print(b)
    # output: peped pep is the best

def methods_replace_ex2():
    a = "Hello! Michael Jackson has: 12 characters."
    print(a)
    b = a.replace('!', '').replace(':', '').replace('.', '')
    print(b)

def methods_find():
    name = "dot pepeled"
    print(name.find("pep"), name.find("led"), len(name))
    print("hello Mike".find("Mike"))

def methods_find_ex2():
    # If cannot find the substring in the string
    name = "dot pepeled"
    print(name.find('pesdfasdasdf'))

def methods_split():
    # split - разделение
    # Split the substring into list
    name = "doted peped"
    split_string = name.split("ed")
    print(f"after: {split_string}, before:{name}")

def test1():
    print(str(1 + 1))
    print( "123".replace("12", "ab"))

test1()