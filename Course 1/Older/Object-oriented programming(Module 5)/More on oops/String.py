class iostring:
    def __init__(self):
        self.str=''
    def inputstring(self):
        self.str=input("Enter a string \n")
    def case(self):
        print(self.str.upper())
nivaan=iostring()
nivaan.inputstring()
nivaan.case()