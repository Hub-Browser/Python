n=int(input("Enter a number:"))
ln=[]
for i in range(1,n+1,2):
    ln.append(i)
lf=["apple","orange","banana"]
lfn=[]
for i in lf:
    lfn.append(i[0].upper()+i[1:])
print(list(zip(ln,lfn)))

