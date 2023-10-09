# Вывод данных на экране и спрашивание информацией и корректировка Имени и пробелов

# Ask user for their name
# = это присваивание чему то
# name - в моем случае это контейнер - тоесть переменая которому дали имя
# print, input - функций
# Remove whitespace from str and capitalize users name .strip().title()
name = input("Whats Your Name?: ").strip().title()
age = input(f"Age? {name}: ")
gmail = input("Gmail: ")

# Say hello to user
# + можно добовлять бесконечно + добавление
# чтобы дать переменую нам нужно использовать {*} и еще добавить в начало знак f чтобы показать ему что это переменая
print(f'Hello, {name}, Age: {age} "Adress: {gmail}@gmail.com"')
