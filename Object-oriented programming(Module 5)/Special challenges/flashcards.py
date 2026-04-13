class flashcards:
    def __init__(self):
        print("Welcome to flashcards!")
    def cards(self):
        definit=[]
        word=[]
        r=0
        while True:
            temp=(input("Enter the word for your flashcard "))
            word.append(temp)
            temp2=(input("Enter the definition of the word"))
            definit.append(temp2)
            x=input("do you want to add more flash cards(Y/N)")
            if x=="Y" or "y":
                continue
            elif x=="N" or "n":
                break
            #PROBLEM NOT BREAKING THE WHILE LOOP
            else:
                print("please try again")
            r=x+1
            
    def display(self,x,word,definit):
        for i in range(x):
            print("Your first word is",word[i])
            t=(input("Enter 1 when you want to see its definition "))
            if t==1:
                print(definit[i])
flash=flashcards()
flash.cards()
flash.display()