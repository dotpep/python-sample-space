class MyClass:
    text: str = "Hello"
    number: int = 5

    def get_text(self):
        return f"{self.text=}"

    def set_text(self, new_text: str):
        print(f"{self.text=}")
        self.text = new_text
        return f"now is {new_text=}"


my_class_obj1 = MyClass()  # instance object, class object
print(my_class_obj1.text)

obj1_text = my_class_obj1.text = "Hi World"
print(obj1_text)

print(my_class_obj1.number)
list_hello_obj1 = [obj1_text[x] for x in range(my_class_obj1.number)]
print(list_hello_obj1)

print(my_class_obj1.text)
print(my_class_obj1.set_text("New Hi"))
