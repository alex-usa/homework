import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, _cords = [0, 0, 0]):
        self.speed = speed
        self._cords = _cords

    def move(self, dx, dy, dz): # который должен менять соответствующие кооординаты в _cords на dx, dy и dz в том же
                                # порядке, где множетелем будет являтся speed. Если при попытке изменения координаты
                                # z в _cords значение будет меньше 0, то выводить сообщение "It's too deep, i can't
                                # dive :(" , при этом изменения не вносятся
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed

        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = dz * self.speed

    def get_cords(self): # который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>,
                        # Z: <координаты по z>"
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self): # который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful,
                        # i'm attacking you 0_0" , если равно или больше
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self): # который выводит строку со звуком sound
        print(self.sound)

class Bird(Animal):
    beak = True # наличие клюва

    def lay_eggs(self): # который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz): # где dz изменение координаты z в _cords. Этот метод должен всегда уменьшать координату z
                            # в _coords. Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
                            # Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного
                            # движения. (speed / 2)
        self._cords[2] = int(self._cords[2] - abs(dz) * (self.speed / 2))

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal): # Порядок наследования определите сами, опираясь на ниже
                                                        # приведённые примеры выполнения кода
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