import random
class Animal:
    live = True
    sound = None # звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0 # степень опасности существа
    def __init__(self,_cords,speed):
        self._cords=[0,0,0]
        self.speed =(self)
    def move(self, dx, dy, dz):
        self._cords=
        pass
    def get_cords(self):
        pass
    def attack(self):
        pass

class Bird(Animal):
    beak = True # наличие клюва
    def lay_eggs(self):
        self.lay_eggs=random(1,4)
        return f'Here are(is)'{self.lay_eggs}'eggs for you'

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz) :

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"




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