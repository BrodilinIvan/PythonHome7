"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные
атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} {self.speed}')

    def go(self):
        print(f'{self.color} {self.name} движется')

    def stop(self):
        print(f'{self.name} остановился')

    def turn_left(self):
        print(f'{self.name} повернул налево')

    def turn_rigth(self):
        print(f'{self.name} повернул направо')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость превышена на {self.speed - 60}! '
                  f'Снизьте скорость!')
        else:
            print(f'Текущая скорость автомобиля {self.name}c{self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Скорость превышена на {self.speed - 40}! '
                  f'Снизьте скорость!')
        else:
            print(f'Текущая скорость автомобиля {self.name}c{self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(65, 'зеленый', 'Матиз', False)
car2 = SportCar(100, 'красный', 'Порше', False)
car3 = WorkCar(45, 'белый', 'ГАЗ', False)
car4 = PoliceCar(110, 'белый', 'Камри', True)
car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()
car1.go()
car1.turn_left()
car1.turn_rigth()
car1.stop()

