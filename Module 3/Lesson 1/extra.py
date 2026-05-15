def sq(l):
    return 4*l
def rec(l,w):
    return 2*(l+w)

choice=input(("Please choose the shape (a/b):\na. Square\nb. Rectangle\n"))

if choice=="a":
    l=float(input("Enter side length:"))
    print(sq(l))
elif choice=="b":
    l=float(input("Enter length:"))
    w=float(input("Enter width:"))
    print(rec(l,w))
else:
    print("Invalid input")