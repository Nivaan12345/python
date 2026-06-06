class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False
    def borrow(self):
        self.is_borrowed=True
        print("You have borrowed",self.title,)
        if self.is_borrowed==True:
            print("You have successfully borrowed this book")
    def return_book(self):
        self.is_borrowed=False
        print("You have returned",self.title)
        if self.is_borrowed==False:
            print("You have successfully returned this book")

hp=book("Harry Potter and the Chamber of secrets","JK Rowling")
pj=book("Percy Jackson and the lightning thief","Rick Riordan")
hv=book("H.I.V.E-The Overlord Protocol","Mark Walden")

hp.borrow()
pj.borrow()
hv.borrow()

hp.return_book()
pj.return_book()
hv.return_book()