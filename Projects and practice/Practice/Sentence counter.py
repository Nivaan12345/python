x=(input("Enter the sentence you want to count the letters in "))
z=len(x)
for i in x:
    if i==' ':
        z=z-1
    else:
        continue
print(z)