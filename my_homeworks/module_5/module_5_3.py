#  Домашняя работа  "Перегрузка операторов."


class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floor:
            for i in range(new_floor):
                i += 1
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название {self.name}, кол-во этажей: {self.number_of_floor}'

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floor = self.number_of_floor + other.number_of_floor
            self.name = self.name + ' + ' + other.name
        if isinstance(other, int):
            self.number_of_floor = self.number_of_floor + other
        return self

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floor = self.number_of_floor + other
        return self

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floor = self.number_of_floor + other
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10  # add
print(h1)
print(h1 == h2)
h1 += 10  # __iadd__
print(h1)
h2 = 10 + h2  # __radd__
print(h2)
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
print()