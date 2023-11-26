file = open('test.txt', mode='r')

data = file.readline()
print(type(file))
print(type(data))
print(dir(file))
# print(help(file))

print(data)

file.close()

with open('test.txt', mode='r') as file:
    data = file.readline()
    print(data)
