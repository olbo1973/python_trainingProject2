## Домашнее задание по теме "Очереди для обмена данными между потоками."
# Задача "Потоки гостей в кафе"

import random  # Импортируем модуль для генерации случайных чисел
import time  # Импортируем модуль для работы со временем
from threading import Thread  # Импортируем класс Thread для работы с потоками
from queue import Queue  # Импортируем класс Queue для работы с очередями


# Класс для представления стола
class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость, сидящий за столом (по умолчанию None)


# Класс для представления гостя, который наследуется от Thread
class Guest(Thread):
    def __init__(self, name):
        super().__init__()  # Инициализация родительского класса Thread
        self.name = name  # Имя гостя

    # Метод, который выполняется при запуске потока
    def run(self):
        wait_time = random.randint(3, 10)  # Генерация случайного времени ожидания от 3 до 10 секунд
        time.sleep(wait_time)  # Пауза, имитирующая время, проведенное гостем за столом


# Класс для представления кафе
class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для ожидания гостей
        self.tables = tables  # Список столов в кафе

    # Метод для прибытия гостей
    def guest_arrival(self, *guests):
        for guest in guests:  # Для каждого гостя в списке гостей
            seated = False  # Переменная для проверки, сидит ли гость за столом
            for table in self.tables:  # Проходим по всем столам
                if table.guest is None:  # Если стол свободен
                    table.guest = guest  # Назначаем гостя за стол
                    guest.start()  # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")  # Сообщаем, что гость сел за стол
                    seated = True  # Гость успешно сел за стол
                    break  # Выходим из цикла по столам
            if not seated:  # Если гость не смог сесть за стол
                self.queue.put(guest)  # Помещаем его в очередь
                print(f"{guest.name} в очереди")  # Сообщаем, что гость в очереди

    # Метод для обслуживания гостей
    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:  # Проходим по всем столам
                if table.guest is not None:  # Если за столом есть гость
                    if not table.guest.is_alive():  # Если поток гостя завершил работу
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")  # Сообщаем, что гость ушел
                        print(f"Стол номер {table.number} свободен")  # Сообщаем, что стол освободился
                        table.guest = None  # Освобождаем стол

                        # Если очередь не пуста, берем следующего гостя из очереди
                        if not self.queue.empty():
                            next_guest = self.queue.get()  # Берем гостей из очереди
                            table.guest = next_guest  # Сажаем его за освободившийся стол
                            next_guest.start()  # Запускаем поток гостя
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            time.sleep(1)  # Задержка, чтобы избежать постоянной проверки


# Пример выполнения кода
if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()

### Общий обзор:
# - Код моделирует работу кафе с гостями и столами, используя многопоточность.
# - Гости, приходя в кафе, занимают столы или ждут в очереди, если столы заняты.
# - Каждый гость задерживается на случайное время, что имитирует время, проведенное за столом.