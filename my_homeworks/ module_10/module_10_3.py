## Домашнее задание по теме "Блокировки и обработка ошибок"
# Задача "Банковские операции"

import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            y = random.randint(50, 500)
            with self.lock:
                self.balance += y
                print(f'Пополнение: {y}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            x = random.randint(50, 500)
            print(f'Запрос на {x}')
            with self.lock:
                if self.balance >= x:
                    self.balance -= x
                    print(f'Снятие: {x}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')