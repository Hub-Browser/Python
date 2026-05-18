n=int(input("Enter the number:"))

for i in range(n,0,-1):
    if i%5==0:
        print("Divisible")
        continue
    else:
        print(i)