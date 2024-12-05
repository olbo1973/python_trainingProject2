# Домашнее задание по теме "Позиционирование в файле".
# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            byte_position = file.tell()  # Получаем текущую позицию в байтах
            file.write(string + '\n')  # Записываем строку в файл с новой строки
            strings_positions[(index, byte_position)] = string  # Сохраняем информацию в словарь

    return strings_positions


# Пример использованию функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

### Объяснение реализации:
# 1. ** Импорт функции **:
# Мы объявили функцию `custom_write`, которая принимает два аргумента: `file_name` и `strings`.
#
# 2. ** Инициализация словаря **:
# Создаем пустой словарь `strings_positions`, чтобы хранить информацию о каждой строке.
#
# 3. ** Открытие файла **:
# Используем контекстный менеджер `with` для открытия файла в режиме записи (`'w'`) с кодировкой `utf-8`.
#
# 4. ** Цикл по строкам **:
# Для каждой строки в списке `strings`:
# - Получаем текущую позицию в байтах с помощью метода `tell()`.
# - Пишем строку в файл, добавляя символ новой строки.
# - Добавляем информацию в словарь `strings_positions` с использованием кортежа `(номер строки, байт начала строки)`
# в качестве ключа.
#
# 5. ** Возврат и вывод **:
# Возвращаем словарь и выводим его содержимое в формате, указанном в примере.
#
# ### Пример вывода:
#
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')
#
# Это показывает, что строки были успешно записаны в файл, и был получен желаемый формат результата.