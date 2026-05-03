char=input("Enter a character: ")
if "a"<=char<="z" or "A"<=char<="Z":
    print(f"{char} is an alphabet")
try:
    if -2147483648<=int(char)<=2147483648:
        print(f"{char} is a digit")
except Exception as e:
    print(f"{char} is a special character")