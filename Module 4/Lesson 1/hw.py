def sql():
    try:
        l=[]
        le=[]
        lo=[]
        lb=int(input("Enter lower bound of list:"))
        ub=int(input("Enter upper bound of list:"))
        for i in range(lb,ub+1):
            l.append(i**2)
            if i%2==0:
                le.append(i)
            elif i%2!=0:
                lo.append(i)
            else:
                print("Invalid")
        print("Square values are:")
        for i in l:
            print(i,end=", ")
        print("\nOdd values are:")
        for i in lo:
            print(i,end=", ")
        print("\nEven values are:")
        for i in le:
            print(i,end=", ")
        print("\n")
    except:
        print("Error")

while True:
    sql()