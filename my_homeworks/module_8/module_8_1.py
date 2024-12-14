
def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        return str(a) + str(b)
    else:
        return result

def convert_input(value):
    try:
        return float(value)
    except ValueError:
        return value  # Возвращать оригинальное значение, если не удаётся преобразовать

# Получаем пользовательский ввод
a_ = input('Введите значение a: ')
b_ = input('Введите значение b: ')

# Преобразуем вводы
a = convert_input(a_)
b = convert_input(b_)

# Выводим результат
print(add_everything_up(a, b))

# Тестовые примеры
print(add_everything_up(123.456, 'строка'))  # Выведет: 123.456строка
print(add_everything_up('яблоко', 4215))     # Выведет: яблоко4215
print(add_everything_up(123.456, 7))          # Выведет: 130.456