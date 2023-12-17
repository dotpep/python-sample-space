country = "USA"
print("Country name: ", country, id(country))

print("-----")
print(globals())
print("-----")

# `comment me` uncomment this check output how scoping works!
def my_local_func():
    # global country  # comment me
    # country = "Germany"  # comment me
    print("Country name: ", country, id(country))

    print("-----")
    print(locals())
    print("-----")


my_local_func()
print("Country name: ", country, id(country))
