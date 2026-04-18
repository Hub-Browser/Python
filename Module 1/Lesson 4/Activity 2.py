money=int(input("Please enter your amount: "))
taka_100=money//100
taka_50=(money%100)//50
taka_10=((money%100)%50)//10
print("Notes of taka 100:",taka_100)
print("Notes of taka 50:",taka_50)
print("Notes of taka 10:",taka_10)