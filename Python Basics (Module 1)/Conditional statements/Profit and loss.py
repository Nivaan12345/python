cost=float(input("enter the cost of your item "))
sell=float(input("enter the price you sold it at "))
if(cost<sell):
    profit=int(sell-cost)
    print("You have made a profit of Rupees",profit)
else:
    loss=int(cost-sell)
    print("you have made a loss of Rupees",loss)
#end