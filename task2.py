# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.

class Road:
    length: int
    width: int

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def weight(self, thickness):
        return int(thickness) * 25 * int(self.width) * int(self.length)


_length = input("Enter length:  ")
_width = input("Enter width:  ")
_Road = Road(_length, _width)
_Weight = _Road.weight(1) # 1 cm
print(f"Mass is ", _Weight)
