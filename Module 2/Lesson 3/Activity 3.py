n=int(input("Enter the number"))
sum=0
temp=n
while temp>0:
    d=temp%10
    sum=sum+d**3
    temp=temp//10
if sum==n:
    print(f"{n} is an armstrong number")
else:
    print("Not armstrong")