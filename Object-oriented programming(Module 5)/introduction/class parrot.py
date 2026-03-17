class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
parakeet=parrot("Parakeet",11)
macaw=parrot("Macaw",15)
print(parakeet.species)
print(macaw.age)