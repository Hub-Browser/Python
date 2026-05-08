def date():
    while True:
        y=int(input("Enter the year: "))
        m=int(input("Enter the month: "))
        d=int(input("Enter the day: "))
        if (not 0<m<13) and (not 0<d<32):
            return print("Not a valid date")
        mlist=["1","3","5","7","8","10","12"]
        d+=1
        if (d==32 and m in mlist) or (d==31 and m not in mlist):
           d=1
           m+=1
           if m==13:
               m=1
               y+=1

