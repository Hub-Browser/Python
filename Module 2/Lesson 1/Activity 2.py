unit=int(input("Enter units consumed:"))
if unit<50:
    total=unit*2.6+25
elif unit<100:
    total=unit*3.25+35
elif unit<200:
    total=unit*4.26+45
else:
    total=unit*8.45+75
print(f"Electricity Bill:{total}BDT")