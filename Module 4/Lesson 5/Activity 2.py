name=["Tim","Bill","Jake","Carl","Zam"]
roll_no=[20, 14, 17, 8, 5]
print(list(zip(name,roll_no)))

for x,y in zip(name,roll_no[::-1]):
    print(x,y)

dict1={
    name:roll_no for name,roll_no in zip(name, roll_no)
}
print(dict1)