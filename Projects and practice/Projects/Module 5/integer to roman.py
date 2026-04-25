class roman_number:
    def converter(self):
        x=int(input("Enter a number to convert "))
        y={1:'I',5:'V',10:'X',50:'L',100:'C',1000:'M',500:'D',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        print(y[x])
obj=roman_number()
obj.converter()
#end