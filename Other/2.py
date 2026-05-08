def date():
    while True:
        y=int(input("Enter the year: "))
        m=int(input("Enter the month: "))
        d=int(input("Enter the day: "))
        if (not 0<m<13) and (not 0<d<32):
            return print("Not a valid date")
        mlist=["1","3","5","7","8","10","12"]
        d+=1
        if (d==32 and m in mlist) or (d==31 and m not in mlist) or ((d==29 and m==2 and y%4==0) and (y%100!=0 or y%400==0)):
           d=1
           m+=1
           if m==13:
               m=1
               y+=1
        print(f"")
date()


