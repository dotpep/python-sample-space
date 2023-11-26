# global scope
my_global = 10

def func1():
    enclosed_v = 8
    # my_global = 1

    def func2():
        local_v = 5
        # my_global = 1
        print("Access to Global", my_global)
        print("Access to Enclosed", enclosed_v)

    func2()


func1()
# print("Cant access to Local", local_v)
# print("Cant access to Enclosed", enclosed_v)
# func2()



x = 300
def myfunc():
  x = 200
  print("Local scope x Variable in myfunc()", x)

myfunc()
print("Global scope variable x", x)



def myfunc():
  global x
  x = 300

myfunc()
print("local x but with (global)", x)


# if you want make change for Global scope var inside function (local scope) use global in local scope for var
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print("change global scope val with (global keyword) inside func (local scope) ", x)


list = [1, 2, 3, 4]
my_tuple = (1, "string", 4.5, True)

list.reverse()
