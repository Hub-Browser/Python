try:
    num=int(input("Enter a number:"))
    print("The number you chose is:",num)
except ValueError as e:
    print("ValueError:",e)