def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(f"The factorial of 1 is {fact(1)}")
print(f"The factorial of 4 is {fact(4)}")
print(f"The factorial of 5 is {fact(5)}")