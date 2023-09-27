import random
print("Please select rock, paper, or scissors")
p1answer = input("> ")
options = ["rock", "paper", "scissors"]
p2answer = random.choice(options)
print("Your opponent chose "+p2answer)
if p1answer == "rock":
    if p2answer == "rock":
        print("Tie")
    else:
        if p2answer == "paper":
            print("You lose")
        else:
            if p2answer == "scissors":
                print("You win")
if p1answer == "paper":
    if p2answer == "rock":
            print("You win")
    else:
        if p2answer == "paper":
            print("Tie")
        else:
            if p2answer == "scissors":
                        print("You lose")
if p1answer == "scissors":
    if p2answer == "rock":
        print("You lose")
    else:
        if p2answer == "paper":
            print("You win")
        else:
            if p2answer == "scissors":
                print("Tie")
