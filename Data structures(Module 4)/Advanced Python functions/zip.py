x=[235,367,375,376,568]
y=['Nivaan','Yurav','Arhan','Bhadra']
res=zip(x,y)
print(list(res))
w=['Prithvi','Ruhan','Prehaan','Hridaan']
z=[975,1046,764,865]
for x,y in zip(w,z[::-1]):
    print(x,y)