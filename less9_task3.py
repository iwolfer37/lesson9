# 3 завдання:
class Parallelogram:
    def __init__(self, width, length):
        # Два аргументи - width та length
        self.width = width
        self.length = length
    def get_area(self):
        # Метод get_area вираховуєм площу паралелограму.
        return self.width * self.length

class Square(Parallelogram):
    def __init__(self, side):
        # Один аргумент для квадрата - side. Бо сторони рівні
        super().__init__(side, side)

    def get_area(self):
        return super().get_area()

# перевірка роботи для паралелограму ми взяли 10 й 20, для квадрату 10:
parallelogram = Parallelogram(10, 20)
print(f"Площа паралелограма: {parallelogram.get_area()}")
square = Square(10)
print(f"Площа квадрата: {square.get_area()}")
