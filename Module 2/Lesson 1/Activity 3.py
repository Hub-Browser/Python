ride=int(input("Select your ride (1/2)\n1. Bike\n2. Car"))
if ride==1:
    rid=int(input("Select your ride (1/2)\n1. Motorcycle\n2. Bycicle"))
    if rid==1:
        print("Your ride is Motorcycle")
    if rid==2:
        print("Your ride is Bycicle")
elif ride==2:
    rid=int(input("Select your ride (1/2)\n1. Self driving car\n2. Normal car"))
    if rid==1:
        print("Your ride is Self driving car")
    if rid==2:
        print("Your ride is Normal car")