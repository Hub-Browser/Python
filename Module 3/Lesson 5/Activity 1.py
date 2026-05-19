import random
r=random.Random()
playing=True
number=r.randint(1,9)

print("I will generate a number from 1 to 9 and you need to guess the number one digit at a time")

while playing:
    guess=int(input("Guess the number:"))
    if guess==number:
        print("You win the game")
        print("The number was:",number)
        break
    else:
        print("Incorrect! Try again")