print("Enter marks in 5 subjects")
total=0
for i in range(1,6):
    mark=int(input(f"Enter makrs in subject{i}"))
    total+=mark
avg=total/5
a=101
b=110
listt=["A1","A2","B1","B2","C1","C2","D","E1","E2"]
for i in range(1,10):
    a-=10
    b-=10
    if avg>=a and avg<=b:
        print("Your grade is",listt[i-1])

    