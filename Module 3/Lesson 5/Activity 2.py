import random
r=random.Random()

while True:
    user_action=input("Enter a choice (rock, paper, scissors):").lower()
    possible_actions=["rock", "paper", "scissors"]
    computer_action=r.choice(possible_actions)
    print(f"Your choice:{user_action}\nComputer's choice:{computer_action}")

    if user_action==computer_action:
        print("Its a tie!")
    elif user_action=="rock":
        if computer_action=="paper":
            print("Paper covers the rock. You lose!")
        else:
            print("Rock smashes scissors. You win!")

    elif user_action=="paper":
        if computer_action=="rock":
            print("Paper covers the rock. You win!")
        else:
            print("Scissors cuts paper. You lose!")

    elif user_action=="scissors":
        if computer_action=="paper":
            print("Scissors cuts paper. You win!")
        else:
            print("Rock smashes scissors. You lose!")
    
    playagain=input("Want to play again (y/n):").lower()
    if playagain=="n":
        break


