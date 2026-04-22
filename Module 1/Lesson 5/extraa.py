
age=int(input("Enter age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

num=int(input("Enter score"))
if num>=50:
    print("Pass")
else:
    print("Fail")

char=input("Enter a character: ")
vow="aeiou"
if char in vow:
    print("Vowel")
else:
    print("Consonant")

sum=0
for i in range(1,4):
    angle=float(input("Enter an angle: "))
    sum+=angle
if sum==180:
    print("Triangle is valid")
else:
    print("Triangle is invalid")