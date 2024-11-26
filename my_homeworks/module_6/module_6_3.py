import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self._cords[2] -= dz  # Always reduce z coordinate
        self.speed = self.speed / 2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

    def speak(self):
        print(self.sound)


# Пример работы программы:
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

### Объяснение класса Duckbill: - Мы наследуем класс `Duckbill` из `PoisonousAnimal`, `Bird`, `AquaticAnimal`.Порядок
# наследования определен так, чтобы `PoisonousAnimal` был выше, т. к. утконос ядовит и было предупреждение об этом.
#  Метод `speak` добавлен в `Duckbill`, чтобы выводить звук, который издает утконос.

### Пример работы программы:
# 1. Утконос создается со скоростью 10. 2.Проверяем состояние объектов и их
# атрибуты: `live` и `beak`. 3. Выводим звук утконоса и его реакцию на атаку. 4. Перемещаем утконоса и выводим его
# координаты. 5.Утконос ныряет и координаты снова проверяются. 6. Утконос откладывает яйца, а число яиц генерируется
# случайным образом.