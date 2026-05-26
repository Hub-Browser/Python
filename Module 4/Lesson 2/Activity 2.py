def pal(x):
    e=len(x)-1
    s=0
    while s<e:
        if x[s]!=x[e]:
            return False
        s+=1
        e-=1
    return True
x=(1,2,3,3,2,1)
if pal(x):
    print("Palindrome")
else:
    print("Not a Palindrome")
