class india:
    def __init__(self,type,capital,language):
        self.capital=capital
        self.type=type
        self.language=language
    def typex(self):
        print(f"India is a {self.type} country")
    def capitalx(self):
        print(f"India's capital is {self.capital}")
    def languagex(self):
        print(f"India's language is {self.language}")

class myanmar:
    def __init__(self,type,capital,language):
        self.capital=capital
        self.type=type
        self.language=language
    def typex(self):
        print(f"Myanmar is a {self.type} country")
    def capitalx(self):
        print(f"Myanmar's capital is {self.capital}")
    def languagex(self):
        print(f"Myanmar's language is {self.language}")      

class pakistan:
    def __init__(self,type,capital,language):
        self.capital=capital
        self.type=type
        self.language=language
    def typex(self):
        print(f"Pakistan is a {self.type} country")
    def capitalx(self):
        print(f"Pakistan's capital is {self.capital}")
    def languagex(self):
        print(f"Pakistan's language is {self.language}")

x=india("developing","New dehli","hindi")
y=myanmar("developing","Naw pyi daw","burmese")
z=pakistan("developing","Islamabad","Urdu")
for countries in (x,y,z):
    countries.capitalx()
    countries.typex()
    countries.languagex()