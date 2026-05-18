def max():
    try:
        ll=int(input("Enter no of items in list:"))
        for i in range(ll):
            li=int(input("Enter list item:"))
            listt.append(li)
        listt.sort()
        print(listt[ll-1])
    except Exception as e:
        print("Invalid input")

while True:
    listt=[]
    max()