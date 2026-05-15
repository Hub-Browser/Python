def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("Please select one of the following operations:")
print("a. Addition\nb. Subtraction\nc. Multiplication\nd. Division")
choice=input("Enter your choice (a/b/c/d):")

a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

if choice=="a":
    print(f"{a}+{b}={add(a,b)}")
elif choice=="b":
    print(f"{a}-{b}={sub(a,b)}")
elif choice=="c":
    print(f"{a}*{b}={mul(a,b)}")
elif choice=="d":
    print(f"{a}/{b}={div(a,b)}")
else:
    print("Invalid choice")