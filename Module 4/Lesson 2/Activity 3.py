weather=(1,0,0,0,1,1,0)
rainy=0
sunny=0

for i in range(0,7):
    if weather[i]==0:
        sunny+=1
    else:
        rainy+=1
if sunny>rainy:
    print("The weather is good")
else:
    print("The weather is bad")