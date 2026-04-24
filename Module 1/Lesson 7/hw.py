ascii=input("Enter a character: ")
if len(ascii)==1:
    ordd=ord(ascii)
    print("Character ASCII value is",ordd)
    if ordd>=48 and ordd<=57:
        print("Type: Digit")
    elif ordd>=65 and ordd<=90:
        print("Type: Uppercase Letter")
    elif ordd>=97 and ordd<=122:
        print("Type: Lowercase Letter")
    elif ordd==32:
        print("Type: Space")
    else:
        print("Type: Special Character")
    



