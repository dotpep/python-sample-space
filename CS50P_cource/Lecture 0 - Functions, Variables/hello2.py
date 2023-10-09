# Вывод данных на экране и спрашивание информацией и корректировка Имени и пробелов

# Ask user for their name
# Remove whitespace from str and capitalize users name .strip().title()
name = input("Whats Your Name?: ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {first}")
