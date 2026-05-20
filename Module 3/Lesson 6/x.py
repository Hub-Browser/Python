def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    try:
        a=float(input("Enter the 2 numbers and the operation:\nNumber 1:"))
        b=float(input("Number 2:"))
        op=input("Operation:")

        if len(op)!=1:
            print("Invalid operation")
            continue
        elif "+" in op:
            print(add(a,b))
        elif "-" in op:
            print(sub(a,b))
        elif "*" in op:
            print(mul(a,b))
        elif "/" in op:
            print(round(div(a,b),3))
        else:
            print("Invalid input")

    except ValueError:
        print("That is not a number!")
    except ZeroDivisionError:
        print("You cannot divide by zero!")