# Напишіть клас автомобіля з атрибутами
class Car:
    # Наші атрибути ініціалізуєм при створені класу:
    def __init__(self, brand, color, engine_size):
        self.brand = brand
        self.color = color
        self.engine_size = engine_size
    def go_forward(self):
        print(f"{self.color} {self.brand} їде вперед.")
    def go_back(self):
        print(f"{self.color} {self.brand} їде назад.")
my_car = Car('Toyota', 'Чорна', 2.0)
my_car_2 = Car('Nissan', 'Білий', 2.5)
my_car_3 = Car('Peugeot', 'Cиній', 1.5)
my_car.go_forward()
my_car_2.go_back()
my_car_3.go_forward()

# ще один клас успедкований від попереднього з новими методами повроту в ліво та право
class TurnCar(Car):
    def turn_l(self):
        print(f"{self.color} {self.brand} повертає ліворуч.")
    def turn_r(self):
        print(f"{self.color} {self.brand} повертає праворуч.")
my_turn_car = TurnCar('Honda', 'Сіра', 1.5)
my_turn_car2 = TurnCar('Nissan', 'Білий', 2.5)
my_turn_car.go_forward()
my_turn_car2.turn_l()
my_turn_car.turn_r()



