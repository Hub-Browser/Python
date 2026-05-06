n=input("Enter a number: ")
l=len(n)
sum=0
i=1
while i<=l:
    sum+=int(n[i-1])
    i+=1
print(sum)

