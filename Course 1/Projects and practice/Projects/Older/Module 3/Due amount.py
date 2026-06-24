bill=float(input("Enter the total bill amount in Rupees "))
amount_given=int(input("Enter the amount you gave in Rupees "))
def due_amount(bill,amount_given):
    change=amount_given-bill
    print("You have to give",change,"in Rupees")
    return change
due_amount(bill,amount_given)
#end