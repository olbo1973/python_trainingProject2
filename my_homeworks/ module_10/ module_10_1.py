## Домашнее задание по теме "Введение в потоки".
# Задача "Потоковая запись в файлы"


# Импорты необходимых модулей
from time import sleep
from datetime import datetime
from threading import Thread

# Объявление функции write_words
def write_words(word_count, file_name):
    """Записывает указанное количество слов в файл с паузой между записями."""
    with open(file_name, 'w', encoding='utf-8') as file:  # 'w' для перезаписи
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

# Взятие текущего времени
time_start = datetime.now()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
time_stop = datetime.now()
time_res = time_stop - time_start

# Вывод разницы начала и конца работы функций
print(f'Время работы функций {time_res}')

# Взятие текущего времени
time2_start = datetime.now()

# Создание и запуск потоков с аргументами из задачи
args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

threads = []
for arg in args:
    thread = Thread(target=write_words, args=arg)
    threads.append(thread)
    thread.start()

# Ожидаем завершения всех потоков
for thread in threads:
    thread.join()

# Взятие текущего времени
time2_stop = datetime.now()
time2_res = time2_stop - time2_start
print(f'Время работы потоков {time2_res}')

# Вывод разницы начала и конца работы потоков
if time_res > time2_res:
    print(f'Использование потоков быстрее функций на {time_res - time2_res} секунд')
else:
    print('Использование потоков не было быстрее функций')