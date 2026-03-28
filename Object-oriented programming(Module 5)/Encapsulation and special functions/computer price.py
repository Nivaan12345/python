class computer:
    def __init__(self):
        self.__max_price=2341
    def sell(self,price):
        self.__max_price=price
        print(f"the price the computer wil be sold is {self.__max_price}")


x=int(input("Enter the sell price "))
lenovo=computer()
lenovo.sell(x)