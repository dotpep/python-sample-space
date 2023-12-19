def slicing_first_three():
    box = "ABCDEFG"
    print(box[:3])


def every_second_char():
    box = 'clocrkr1e1c1t'
    print(box[::2])


def back_slash_print():
    print("dsadas \\dada")
    print(r"dada \ dada")


def convert_uppercase():
    box = "Your are wrong"
    print(box.upper())


def conver_lowercase():
    f2 = "YOU ARE RIGHT"
    print(f2.lower())


g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"


def find_first_index_sub_string():
    print(g.find("snow"))


def replace_sub_string():
    print(g.replace("Mary", "Bob"))
    print(g.replace(",", "."))


def split_sub_string():
    print(g.split())


split_sub_string()
