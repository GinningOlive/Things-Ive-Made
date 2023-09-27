import random
def main():
	print("Please select rock, paper, or scissors")
	p1answer = input("> ")
	options = ["rock", "paper", "scissors"]
	p2answer = random.choice(options)
	print("Your opponent chose "+p2answer)
	if p1answer == "rock":
    		if p2answer == "rock":
        		result = "Tie"
    		else:
        		if p2answer == "paper":
            			result = "You lose"
        		else:
            			if p2answer == "scissors":
                			result = "You win"
	if p1answer == "paper":
    		if p2answer == "rock":
            		result = "You win"
    		else:
        		if p2answer == "paper":
            			result = "Tie"
        		else:
            			if p2answer == "scissors":
                        		result = "You lose"
	if p1answer == "scissors":
    		if p2answer == "rock":
        		result = "You lose"
    		else:
        		if p2answer == "paper":
            			result = "You win"
        		else:
            			if p2answer == "scissors":
                			result = "Tie"
	if result == "Tie":
		print("Try again")
		main()
	else:
		print(result)
		print("Would you like to play again?")
		repeat = input("> ")
		if repeat == "yes":
			main()
		else:
			print("Thank you for playing")
			exit()
main()
