n=1
while n<=500:
    my_way=(n/2)*(n+1)
    trad=0
    for i in range(n+1):
        trad+=i
    if my_way==trad:
        continue
    else:
        print("It's alright,at least your method works till the number",n)
        exit()
    n+=1
print("Let's go,you did it!")