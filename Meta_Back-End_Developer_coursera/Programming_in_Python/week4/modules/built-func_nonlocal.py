# `comment me` uncomment this check output how scoping works!
def func():
    # global animal  # comment me
    animal = "2. elephant"

    def nested_func():
        nonlocal animal  # comment me
        # global animal  # comment me
        animal = "3. giraffe"
        print("3. Inside nested function: ", animal, id(animal))

    print("2. Before calling function", animal, id(animal))
    nested_func()
    print("2. After calling function", animal, id(animal))


animal = "1. camel"
func()
print("1. Global animal: ", animal, id(animal))
