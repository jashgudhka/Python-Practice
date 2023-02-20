import random

#These 2 variables, namely "user_wins" and "computer_wins" will help us track the number of rounds each of them has won.
user_wins = 0
computer_wins = 0

#This is a list to create the options for the game. We will use this list as we go further.
#Rock = 0, Paper = 1, Scissors = 2
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors to play.\nOr Type Q to quit the game.\n").lower()
    if user_input == "q":
        break
    #This condition will do a validation check, whether the user has entered the correct type of input or not. If the user did not enter the correct form of input, it will prompt the user to enter a valid input and go back to the starting point of the while loop.
    elif user_input not in options:
        print("Please enter a valid input")
        continue
    elif user_input in options:
        
        #Creating a random number variable to generate the number for computer's input.
        r_number = random.randint(0,2)
        pc_input = options[r_number]
        print("Computer chose", pc_input + ".")
        
        if user_input == options[0] and pc_input == options[2]:
            print("Congrats, you win!")
            user_wins += 1
        elif user_input == options[1] and pc_input == options[0]:
            print("Congrats, you win!")
            user_wins += 1
        elif user_input == options[2] and pc_input == options[1]:
            print("Congrats, you win!")
            user_wins += 1
        elif user_input == pc_input:
            print("You and Computer chose the same option. It's a tie!")
        else:
            print("Computer wins!")
            computer_wins += 1

print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Goodbye!")