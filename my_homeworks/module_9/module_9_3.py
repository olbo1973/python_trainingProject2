## Домашнее задание по теме "Генераторные сборки"


# Даны два списка строк
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Создание генераторной сборки, которая высчитывает разницу длин строк, если их длины не равны
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка, которая содержит результаты сравнения длин строк в одинаковых позициях
second_result = (len(first[i]) != len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))   # [1, 2]
print(list(second_result))  # [False, False, True]
