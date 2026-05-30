dict={
    "Codingal":"3",
    "is":"2",
    "best":"2",
    "for":"2",
    "coding":"1"
}
k=input("Enter the value:")
result=0
for key in dict:
    if dict[key]==k:
        result+=1
print("The frequency is",result)
