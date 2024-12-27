## Домашнее задание по теме "Потоки на классах"
# Задача "За честь и отвагу!"

import threading
import time


class Knight(threading.Thread):
    total_enemies = 100  # Общее количество врагов

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemies_remaining = Knight.total_enemies

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies_remaining > 0:
            time.sleep(1)  # Задержка в 1 секунду
            self.days += 1
            self.enemies_remaining -= self.power
            if self.enemies_remaining < 0:
                self.enemies_remaining = 0
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies_remaining} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание экземпляров класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения битв
first_knight.join()
second_knight.join()

print("Все битвы закончились!")

