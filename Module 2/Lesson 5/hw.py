r=int(input("Enter number of rows:"))
s=" "
for i in range(0,r+1):
    s1=s*(r-i)
    print(s1,end="")
    for j in range(1,i+1):
        print("*",end="")
    print()