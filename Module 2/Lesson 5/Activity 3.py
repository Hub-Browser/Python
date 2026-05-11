r=int(input("Enter number of rows:"))
for i in range(r+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()
for i in range(r+1,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print()