cost=float(input("Enter cost price: "))
sell=float(input("Enter selling price: "))
if (sell>cost):
    amount=sell-cost
    print("He has a profit of ", amount, "tk")
else:
    print("No profit")