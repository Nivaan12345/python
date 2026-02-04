sunny=0
rainy=0
x=(1,0,0,0,1,1,0)
for i in x:
    if i==1:
        rainy=rainy+1
    else:
        sunny=sunny+1
if rainy>sunny:
    print("Tomorrow is going to be rainy")
else:
    print("Tomorrow is going to be sunny")

y=(32,27,31,29,33)
avg=sum(y)/len(y)
if avg>=31:
    print("The weather is hot")
else:
    print("The weather is normal")