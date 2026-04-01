class reverse:
    def __init__(self,s):
        self.s=s
    def reverse(self):
        self.s=self.s[::-1]
        print(f"Your word is now {self.s}")

x=input("Enter the word to reverse ")
word=reverse(x)
word.reverse()