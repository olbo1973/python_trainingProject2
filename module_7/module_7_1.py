# Задача "Учёт товаров"


# Создаём класс Продукты
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


# Создаём класс Магазин
class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                contents = file.read()
                print(contents)
        except FileNotFoundError:
            print("Файл не найден. Продукты отсутствуют.")

    def add(self, *products):
        existing_products = set()

        # Читаем уже существующие продукты
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    existing_products.add(line.strip())  # Добавляем продукты в множество
        except FileNotFoundError:
            pass  # Файл пока не существует, мы просто пропускаем

        for product in products:
            s = str(product)
            if s in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(f'{s}\n')
                    print(f'Продукт {product.name} добавлен в магазин')


# Создание объектов
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Вывод результата
print(p1)
print(p2)  # Проверка __str__

# Добавление продуктов
s1.add(p1, p2, p3)

# Получаем и выводим все продукты из файла
s1.get_products()
