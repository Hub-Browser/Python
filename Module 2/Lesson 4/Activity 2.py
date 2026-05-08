lb=int(input("Enter lower range: "))
ub=int(input("Enter upper range: "))
for i1 in range(lb,ub+1):
    print(i1)
    if i1>1:
        for i2 in range(2,i1):
            if i1%i2==0:
               break
        else:
            print(f"{i1} is a prime number")

