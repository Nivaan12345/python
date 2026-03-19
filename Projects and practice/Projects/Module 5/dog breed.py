class dog:
    animal="dog"
    def __init__(self,breed,colour):
        self.colour=colour
        self.breed=breed
retriever=dog("Golden retriever","gold")
pug=dog("pug","black")
print(retriever.colour,pug.animal,pug.breed)