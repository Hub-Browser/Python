price=float(input("Enter cost of item"))
cash=float(input("Enter available cash"))
if cash>=price:
    print("You can afford the item")
else:
    print("You cannot afford the item")