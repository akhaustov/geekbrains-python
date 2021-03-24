# Урок№6 задание №4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        return f"Текущая скорость {self.name} {self.speed} км\ч"


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f"{self.name} превышает скорость"
        return f"Скорость движения {self.speed} км\ч"


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f"{self.name} превышает скорость"
        return f"Скорость движения {self.speed} км\ч"


class SportCar(Car):
    '''Спортивный автомобиль'''

class PoliceCar(Car):
    '''Полицейская машина'''

town_car = TownCar("BMW", "белый", 70)
town_car.go()
town_car.turn("налево")
town_car.turn("направо")
print(town_car.show_speed())
town_car.stop()
print()

work_car = WorkCar("Бетономешалка", "серый", 40)
work_car.go()
work_car.turn("налево")
work_car.turn("направо")
print(work_car.show_speed())
work_car.stop()

print()
sport_car = SportCar("Bugatti", "черный", 200)
sport_car.go()
sport_car.turn("налево")
sport_car.turn("направо")
print(sport_car.show_speed())
sport_car.stop()





