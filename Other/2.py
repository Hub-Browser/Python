def date():
    while True:
        y=int(input("Enter the year: "))
        m=int(input("Enter the month: "))
        d=int(input("Enter the day: "))
        if (not 0<m<13) or (not 0<d<32):
            return print("Not a valid date")
        mlist=[1,3,5,7,8,10,12]
        if (d==31 and m in mlist) or (d==30 and m not in mlist) or (d==29 and m==2 and ((y%4==0 and y%100!=0) or y%400==0)) or (d==28 and m==2 and not ((y%4==0 and y%100!=0) or y%400==0)):
           d=1
           m+=1
           if m==13:
               m=1
               y+=1
        else: 
            d+=1
        print(f"{y},{m},{d}")
date()


