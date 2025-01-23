## Домашнее задание по теме "Интроспекция"

# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию
# этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#  Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}

def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    obj_attributes = dir(obj)

    # Получаем методы объекта
    obj_methods = [method for method in obj_attributes if callable(getattr(obj, method))]

    # Получаем модуль, к которому объект принадлежит
    obj_module = type(obj).__module__

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': obj_attributes,
        'methods': obj_methods,
        'module': obj_module
    }

    # Выводим информацию в консоль
    print("Информация об объекте:")
    print(f"Тип: {info['type']}")
    print(f"Модуль: {info['module']}")
    print("Атрибуты:")
    for attr in info['attributes']:
        print(f" - {attr}")
    print("Методы:")
    for method in info['methods']:
        print(f" - {method}")

    # Возвращаем информацию об объекте
    return info


# Пример работы:
example_list = ['Это тест', 85, {1: 'a'}, [1, "it's great!", 5.11], 3.14]

for i in example_list:
    number_info = introspection_info(i)
    print(number_info)

