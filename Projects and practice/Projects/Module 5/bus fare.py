class vehicle:
    def __init__(self,seating):
        self.seating=seating
        self.fare=seating*100
class bus(vehicle):
    def __init__(self,maintanance,seating):
        self.maintanance=maintanance

        vehicle.__init__(self,seating)
    def fare(maintanance,seating):
        fare=((maintanance/100)*seating)+seating
        print("the bus fare is",fare)
best=bus(10,50)
best.fare(10,50)