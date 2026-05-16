def cube(num):
    return num**3
def by_3(num):
    if num%3==0:
        return cube(num)
    else:
        return False
print(by_3(3))