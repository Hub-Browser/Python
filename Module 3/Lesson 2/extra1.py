a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
m=max(a,b)

for i in range(m,0,-1):
    if a%i==0 and b%i==0:
        print(f"{i} is the GCD")
        break