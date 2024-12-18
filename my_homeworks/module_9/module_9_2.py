
# Даны два списка строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Сборка списка длин строк из first_strings, которые имеют длину не менее 5 символов
first_result = [len(x) for x in first_strings if len(x) >= 5]

# 2. Сборка списка кортежей, содержащих пары строк из обоих списков с одинаковой длиной
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

# 3. Сборка словаря, где ключ - это строка, а значение - длина строки,
# только для строк из обоих списков с четной длиной
third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 2 == 0}

# Вывод результатов
print(first_result)
#  [10, 8, 8]
print(second_result)
#  [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
print(third_result)
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
