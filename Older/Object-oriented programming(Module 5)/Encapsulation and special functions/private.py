class private:
    _password=21278
    def _privatefunc(self):
        print("My name is Nivaan Jangla")
        print(self._password)
    def hello(self):
        self._privatefunc()
x=private()
x.hello()