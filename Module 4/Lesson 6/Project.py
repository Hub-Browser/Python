data={
    "Alice":60,
    "Bob":78,
    "Carl":89,
    "Dam":64,
    "Emily":74
}
sum=0
for a,b in data.items():
    sum+=b
avg=sum/len(data)
print(f"Class average is {avg}")
maxs=max([b for a,b in data.items()])
maxp=[a for a,b in data.items() if b==maxs]
print(f"Highest scoring student is {maxp[0]} with a score of {maxs}.")
mins=min(b for a,b in data.items())
minp=[a for a,b in data.items() if b==mins]
print(f"Lowest scoring student is {minp[0]} with a score of {mins}.")
while True:
    try:
        ask=input("Enter the name:")
        ask=ask[0].upper()+ask[1:]
        score=data.get(ask,"Student not found")
        if score=="Student not found":
            print(score)
        else:
            print(f"{ask} has a score of {score}.")
    except:
        print("Invalid input")