def tuples_type():
    tuple1 = ('disco11', 11, 1.2)
    print(type(tuple1))


def tuples_index():
    tuple1 = 'disco11', 11, 1.2, "type22", 1 + 2, 22 / 11
    tuple2 = "pep", 22 // 11, int(22 / 11)
    print(f"tuple 1: {tuple1[:4:2]} + self is tuple 2 answer: {tuple2[0]}")
    tuple3 = "tuple 1:", tuple1[0:2], "self is tuple 2 answer:", tuple2[0]
    print(tuple3[-3])
    A = (1, 2, 3, 4, 5)
    print(A[1:4])


def tuples_immutable():
    ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)
    ratings2 = ratings

    ratings = (2, 10, 2)
    rating_sorted = sorted(ratings2)

    print(ratings)
    print(rating_sorted)


def tuples_nesting():
    nesting = (1, (2, 2.5), "three", (2 + 2, 4), (1 + (1 + 0.5) + 2, 4.7), "six", ("seven", (7.5, 7.7, 7.9), "eight",))
    print(nesting[4][0])
    print(nesting[6][1][2])
    print(nesting[6][2][::2])


tuple = ('disco11', [11], 1.2)
print(tuple)
