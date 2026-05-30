dict1={
    "Codingal":2,
    "is":2,
    "best":2,
    "for":2,
    "coding":1
}
print("Original dictionary",dict1)
k=2
res=0
for key in dict1:
    if dict1[key]==k:
        res+=1
print("Frequency of K is:",res)