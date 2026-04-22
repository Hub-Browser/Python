w=float(input("Enter your weight in kg: "))
h=float(input("Enter your height in cm: "))
bmi=w/(h/100)**2
bmi=round(bmi,2)
print(f"Your bmi is {bmi}")
if bmi<=18.4:
    print("You are underweight")
elif bmi<=24.9:
    print("You are normal")
elif bmi<=29.9:
    print("You are overweight")
elif bmi<=34.9:
    print("You are obese")
else:
    print("You are severely obese")