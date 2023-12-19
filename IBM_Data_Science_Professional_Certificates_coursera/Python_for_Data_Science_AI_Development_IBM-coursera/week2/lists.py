def lists():
    lists = ["doted pepedel", 10.1, 1982, [1, 2], ('firsts', 1)]
    print(lists[0][0:3], lists[0][6:9])

    lists.extend(["pop", 10])

    lists2 = lists + [1 + 1, 2, [1.5 + 1.5], 2 * 2]
    print(lists2)


def lists_extend():
    lists = [10.1, 1982, [1, 2], ('firsts', 1)]
    lists.extend(["pop", 10])
    print(lists)


def lists_append():
    lists = [10.1, 1982, [1, 2], ('firsts', 1)]
    lists.append(["dot pep", 10])
    print(lists)
    print(lists[-1][0])


def lists_mutable():
    a = ["disco", 10, 1.2]
    a[0] = "hard rock"
    print(a)


def lists_del():
    a = ["disco", 10, 1.2]
    del (a[0])
    print(a)


def lists_split():
    a = "hard, rock".split()
    print(a)
    print(a[1])
    a = "A, B, C, D".split(",")
    print(a)


def lists_aliasing():
    a = "hard rock", 10, 1.2
    b = a
    # when 2 variable linking 1 tuples or lists named: Aliasing (псевдоним)
    print(a[0], "a - variable")
    print(b[0], "b - variable")


def lists_aliasing2():
    a = ["hard rock", 10, 1.2]
    a[0] = "banana"
    b = a
    print(f"a: {a}, b: {b}, both 0 index changing to banana ")


def lists_aliasing_cloning():
    a = ["hard rock", 10, 1.2]
    # a[0] = "banana": not cloning
    b = a[:]
    a[0] = "banana"  # cloning but now only with: b = a[:] and these Location
    print(f"a: {a}, b: {b}, now variable b not change it is cloning")


lists_aliasing_cloning()

a = ["hard rock", 10, 1.2]
# help(a)

lists_append()
