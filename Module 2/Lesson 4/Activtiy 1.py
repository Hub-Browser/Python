w=input("Enter the word:")
char=input("Enter the character:")
x=0
for i in w:
    if char in i:
        x+=1
print(x)