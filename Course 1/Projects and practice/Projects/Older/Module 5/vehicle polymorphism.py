class BMW:
    def __init__(self,max_speed,fuel_type):
        self.max_speed=max_speed
        self.fuel_type=fuel_type
    def speed(self):
        print("The max speed of a BMW is",self.max_speed)
    def fuel(self):
        print("The fuel in this BMW is",self.fuel_type)

class ferrari:
    def __init__(self,max_speed,fuel_type):
        self.max_speed=max_speed
        self.fuel_type=fuel_type
    def speed(self):
        print("The max speed of a ferrari is",self.max_speed)
    def fuel(self):
        print("The fuel in this ferrari is",self.fuel_type)

fer=ferrari(450,"Speed petrol")
BM=BMW(230,"Diesel")

for cars in (fer,BM):
    cars.speed()
    cars.fuel()