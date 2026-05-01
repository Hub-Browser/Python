med=input("Do you have a medical cause? (y/n): ").lower()
if med=="y":
    print("You are allowed for the exam")
else:
    at=int(input("Enter your attendence: "))
    if at>=75:
        print("You are allowed for the exam")
    else:
        print("Not allowed")