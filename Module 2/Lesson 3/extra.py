n=int(input("Enter a number: "))
x=0
sum=0
while x<n:
    for i in range(0,n-x):
        extra=2*(10**i)
        sum+=extra
    x+=1
print(sum)


    
