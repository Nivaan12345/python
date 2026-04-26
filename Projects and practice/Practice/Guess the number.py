import random
x=[['482', '019', '735', '264', '908', '157', '603', '821', '346', '590'],
   ['274', '860', '391', '047', '529', '618', '702', '135', '984', '266'],
   ['753', '420', '186', '907', '311', '562', '048', '679', '820', '234'],
   ['915', '308', '674', '120', '889', '453', '267', '590', '731', '042'],
   ['668', '259', '804', '137', '492', '375', '901', '726', '018', '543'],
   ['380', '761', '205', '694', '832', '147', '569', '413', '980', '256'],
   ['824', '063', '751', '290', '536', '178', '642', '819', '357', '904'],
   ['495', '210', '683', '972', '134', '758', '046', '621', '870', '389'],
   ['517', '882', '369', '704', '251', '938', '640', '176', '823', '459'],
   ['068', '997', '325', '541', '786', '209', '653', '118', '472', '830']]
y=random.choice(x)
print("Welcome to Guess the Number!!\nIn this game, I the number guesser will try to find your number in a maximum of 10 guesses")
print("The rules:\nYou have to think of a 3 digit number, if your number is 2/1 digits add the 0's before the number to make it 3 digits")
print("When I guess a number you will type 1 for if the first digit is correct,you will type 2 for if the second digit is correct")
print("you will type 3 for if the third digit is correct,and you will type 0 if there are no numbers correct")
print("finally good luck, try your best")
s=""
for i in y:
    temp=int(input(f"my  guess is {i} "))
    for j in range(6):
        if temp==1:
            s=s+(i[0])
            r=input("Do you have more numbers that are correct?(Y/N)")
            if r!='Y'or 'y':
               break
            else:
                print("invalid answer please try again")
            break
        elif temp==2:
            s=s+(i[1])
            r=input("Do you have more numbers that are correct?(Y/N)")
            if r!='Y'or 'y':
                break
            else:
                print("invalid answer please try again")
            break
        elif temp==3:
             s=s+(i[2])
             r=input("Do you have more numbers that are correct?(Y/N)")
             if r!='Y'or 'y':
                break
             else:
                print("invalid answer please try again")
             break
        elif temp==0:
            pass
    if len(s)==3:
        break
print("Yay, I have beaten you your number was",s)
