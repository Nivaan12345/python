bill=int(input("Enter the total bill amount "))
tip_perc=int(input("How much percentage of the bill do you want to tip "))
def total_calc(bill,tip_perc):
    total=(((tip_perc/100)*bill)+bill)
    print("The total amount you have to pay is Rupees",total)
total_calc(bill,tip_perc)
#end