## Домашнее задание по теме "Создание исключений"
# Задача "Некорректность"

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

# Пример выполняемого кода
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

### Объяснение кода:
# 1. **Исключения**:
#    - `IncorrectVinNumber`: это исключение выбрасывается, когда неправильно задан vin-номер.
#    - `IncorrectCarNumbers`: это исключение выбрасывается, когда неправильно заданы номера автомобиля.
#
# 2. **Класс `Car`**:
#    - Конструктор `__init__` получает `model`, `vin`, и `numbers`, а затем вызывает методы валидации `__is_valid_vin` и
# `__is_valid_numbers`.
#    - Методы `__is_valid_vin` и `__is_valid_numbers` проверяют корректность ввода: типы данных и соответствие диапазону
# или длине.
#
# 3. **Примеры создания объектов**:
#    - Каждый блок `try` создает объект `Car`. Если входные данные некорректны, соответствующее исключение будет
# перехвачено, и его сообщение будет выведено на консоль.
