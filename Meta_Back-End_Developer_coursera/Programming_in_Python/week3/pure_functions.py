my_list = [1, 2, 3]


# not pure function cause this func manipulate global scope lists appending new item into list
def add_to_list_not_pure(item):
    my_list.append(item)
    return my_list


# new_list = add_to_list_not_pure(4)

# print(new_list)
# print(my_list)


def add_to_list_pure(lst, item):
    # nl = lst
    nl = lst.copy()
    nl.append(item)
    return nl


new_list = add_to_list_pure(my_list, 4)

print(new_list)
print(my_list)
