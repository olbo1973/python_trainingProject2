## Домашнее задание по теме "Итераторы"
# Задача "Range - это просто":

class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration

        current = self.pointer
        self.pointer += self.step
        return current


# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()

### Объяснение кода:
# 1. Создан класс `StepValueError`, который наследуется от `ValueError`.
# 2. Создан класс `Iterator` с необходимыми атрибутами и методами.
# 3. В методе `__init__` проверяется значение `step`, чтобы убедиться, что оно не равно 0. В случае равенства
# выбрасывается исключение `StepValueError`.
# 4. Метод `__iter__` сбрасывает указатель `pointer` на `start` и возвращает объект итератора.
# 5. Метод `__next__` увеличивает `pointer` на значение `step` и проверяет условия для завершения итерации.
# 6. В основной части кода проверяется работа класса с экземплярами объекта `Iterator`, а также обрабатывается (исключение,
# если) шаг равен 0.