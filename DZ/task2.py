"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    wei = 25  # масса асфальта для покрытия одного кв
    # метра дороги асфальтом, толщиной в 1 см
    th = 0.05  # толщины полотна в м.

    def __init__(self, length, width):
        self._length = length  # длина в метрах
        self._width = width  # ширина в метрах

    def mass_calculation(self):
        print(
            f'Масса асфальта необходимого для покрытия дорожного полотна: '
            f'{int((self._length * self._width * self.wei * self.th) / 1000)} '
            f'тонн')


instance = Road(20, 5000)
instance.mass_calculation()
