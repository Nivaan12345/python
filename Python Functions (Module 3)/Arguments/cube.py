num=int(input("The number you want a cube of "))
def cube(num):
    x=num**3
    return x
def divisiblity(num):
    if num%3==0:
        return cube(num)
    else:
        return False
print(divisiblity(num))