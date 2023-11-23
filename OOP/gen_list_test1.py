import random

class NumberGenerator:
    """
    A class for generating lists of odd and even numbers.

    Methods:
    - generate_odd_numbers(n): Generates a list of odd numbers up to 2n.
    - generate_even_numbers(n): Generates a list of even numbers up to 2n.
    """

    def generate_odd_numbers(self, n):
        return [i for i in range(1, 2 * n + 1, 2)]

    def generate_even_numbers(self, n):
        return [i for i in range(2, 2 * n + 1, 2)]

class NumberManipulator:
    """
    A class for manipulating lists of numbers, such as removing random numbers.

    Methods:
    - __init__(self, numbers): Initializes the object with the given list of numbers.
    - remove_random_numbers(count): Removes random numbers from the list a specified number of times.
    """

    def __init__(self, numbers):
        self.numbers = numbers.copy()

    def remove_random_numbers(self, count):
        for _ in range(min(count, len(self.numbers))):
            self.numbers.remove(random.choice(self.numbers))

class NumberAnalyzer:
    """
    A class for analyzing lists of numbers, finding missing numbers after modification.

    Methods:
    - find_missing_numbers(original_list, modified_list, number_type):
      Static method that compares two lists and prints missing numbers in the modified list.

    Example:
      number_analyzer = NumberAnalyzer()
      number_analyzer.find_missing_numbers(original_list, modified_list, "list_type")
    """

    @staticmethod
    def find_missing_numbers(original_list, modified_list, number_type):
        missing_numbers = [num for num in original_list if num not in modified_list]
        if missing_numbers:
            print(f"In {number_type}, the following numbers are missing: {missing_numbers}")
        else:
            print(f"All {number_type} numbers are present.")

# Создаем NumberGenerator для генерации списков odd и even до 10
number_generator = NumberGenerator()
list_odd = number_generator.generate_odd_numbers(10)
list_even = number_generator.generate_even_numbers(10)

# Создаем NumberManipulator для удаления случайных чисел
number_manipulator_odd = NumberManipulator(list_odd)
number_manipulator_odd.remove_random_numbers(2)

number_manipulator_even = NumberManipulator(list_even)
number_manipulator_even.remove_random_numbers(2)

# Создаем NumberAnalyzer для поиска отсутствующих чисел
number_analyzer_odd = NumberAnalyzer()
number_analyzer_odd.find_missing_numbers(list_odd, number_manipulator_odd.numbers, "list_odd")

number_analyzer_even = NumberAnalyzer()
number_analyzer_even.find_missing_numbers(list_even, number_manipulator_even.numbers, "list_even")
