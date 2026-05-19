while True:
    try:
        age=int(input("Enter age:"))
        if age<1:
            print("Invalid")
            continue
        print("Age is:",age)
        if age%2==0:
            print(f"{age} is even")
        else:
            print(f"{age} is odd")
    except:
        print("Invalid")
     
