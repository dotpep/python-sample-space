import re

s1 = "This is Data Science module named re - regular extension (регулрные выражение)"
s2 = "Binary search algorithm for Data Science"
s3 = "The IBM is huge company in Computer Science sphere - Revenue	Increase US$60.53 billion (2022)"
s4 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"


def sub_string():
    print(re.sub("Data Science", "Artificial Intelligent", s1))
    # replace sub-string "first" with "second" with sub()


def find_all():
    print(re.findall("woo", s4))
    # find all the occurrences of "woo" using findall() function


def search_func():
    result = re.search("\d", s3)  # find digit character with \d and search()
    if result:
        print("Success Found")
    else:
        print("Not found")


sub_string()
