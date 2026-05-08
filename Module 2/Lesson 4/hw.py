dec=int(input("Enter decimal number:"))
bin=bin(dec)
bin=str(bin)
l=len(bin)
bin=bin[2:l]
print(bin)