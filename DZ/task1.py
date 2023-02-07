"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод
running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:

    def __init__(self, color, times):
        self._color = color
        self.times = times

    def running(self):
        print(f'Горит {self._color} свет')
        sleep(self.times)


red = TrafficLight('Красный', 7)
yellow = TrafficLight('Желтый', 2)
green = TrafficLight('Зеленый', 4)

red.running()
yellow.running()
green.running()
