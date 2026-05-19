import math as m

while True:
    try:
        op=input("Enter the operation:").lower()
        n=float(input("Enter the number:"))
        if "sin" in op:
            print(m.sin(n))
        elif "cos" in op:
            print(m.cos(n))
        elif "tan" in op:
            print(m.tan(n))
        else:
            print("No operation specified")
    except:
        print("Invalid input")
