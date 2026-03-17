class vehicle:
    def __init__(self,mileage,max_speed):
        self.mileage=mileage
        self.max_speed=max_speed
car=vehicle(20,250)
print(car.mileage,car.max_speed)