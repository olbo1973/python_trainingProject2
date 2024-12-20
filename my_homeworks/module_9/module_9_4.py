## Домашнее задание по теме "Создание функций на лету"
# Задача "Функциональное разнообразие":


#Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)

# Замыкание:

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:  # Открываем файл в режиме добавления
            for item in data_set:
                f.write(f"{item}\n")  # Записываем каждый элемент с новой строки
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words  # Сохраняем переданные слова в атрибут

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово

# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

# При выполнении программы вывод может варьироваться, поскольку выбор осуществляется случайным образом.