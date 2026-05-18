pasw=input("Enter the password:")
x=0
while True:
    if pasw=="CoDinGal132":
        print("Access granted")
        break
    else:
        print("Incorrect password")
        x+=1
        if x==3:
            break