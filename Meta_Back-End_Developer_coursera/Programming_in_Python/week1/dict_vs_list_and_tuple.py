"""
Поиск будет быстрее в dict и set, потому что это хеш-таблицы, доступ к элементу которых выполняется за O(1).
Для list и tuple поиск будет выполняться в среднем за O(n).

Исключение работает только для очень маленьких списков длиной до 5 элементов.
В этом случае интерпретатору будет быстрей пробежаться по списку, чем считать хеш.
"""
import timeit

l = list(range(1000000))
d = dict.fromkeys(l)
s = set(l)

def iter_list():
    for i in l:
        pass

def iter_dict():
    for i in d:
        pass

def iter_set():
    for i in s:
        pass


print("list: ", timeit.timeit(iter_list, number=1000))
print("dict: ", timeit.timeit(iter_dict, number=1000))
print("set: ", timeit.timeit(iter_set, number=1000))