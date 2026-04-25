class vehicle:
    def __init__(self,seating):
        self.seating=seating
class bus(vehicle):
    def __init__(self,maintanance,seating):
        self.maintanance=maintanance

        vehicle.__init__(self,seating)
    def fare(self,maintanance,seating):
        res=((maintanance/100)*seating)+seating
        print("the bus fare is",res)
best=bus(10,50)
best.fare(10,50)