a=10
b=20
c=30
v=(a+b+c)/3
print("The average speed is",v)
if v>max(a,b,c):
    print(f"{v} is greater than {a} {b} and {c}")
elif v>max(a,b):
    print(f"{v} is greater than {a} and {b}")
elif v>max(b,c):
    print(f"{v} is greater than {b} and {c}")
elif v>max(a,c):
    print(f"{v} is greater than {a} and {c}")
elif v>a:
    print(f"{v} is greater than {a}")
elif v>b:
    print(f"{v} is greater than {b}")
elif v>c:
    print(f"{v} is greater than {c}")
else:
    print("Invalid input")

