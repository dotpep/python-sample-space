scope_g = "1) global"


def func2():
    print("---2) enclosed local func1: ")

    scope_l = "2) enclosed in func1"

    def func3():
        print("--- 3) local func2: ")
        global scope_l
        scope_l = "3) local in func2"
        print("3) local in inner func2", scope_l, id(scope_l))

    print("2) enclosed local outer func1 test1: ", scope_l, id(scope_l))
    func3()
    print("2) enclosed local outer func1 test2: ", scope_l, id(scope_l))

    # print("--- make nonlocal")
    # nonlocal scope_en_f1
    # scope_en_f1 = "nonlocal inside outer func1"
    # print(scope_en_f1)

    print("--- 2) change global")
    global scope_g
    scope_g = "2) change global inside outer func1"
    print("2) ", scope_g, id(scope_g))


print("1) global test1: ", scope_g, id(scope_g))
print("--- 1) function start")
func2()
print("--- 1) function end")
print("1) global test2: ", scope_g, id(scope_g))

print("--- 1) print make global")
print("1) ", scope_l, id(scope_l))
