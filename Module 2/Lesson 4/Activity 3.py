num=int(input("Enter a number:"))
if num>=4:
    num=str(num)
    l=len(num)
    if l%2!=0:
        l=int((l/2)+1)
    else:
        l=int(l/2)
    m1=int(num[l-1])
    m2=int(num[l])
    p=m1*m2
    print(p)