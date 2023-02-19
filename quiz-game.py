print("Welcome for to my computer Quiz Gamex!")

playing = input("Do you want to play? ") #Prompting the user to check whether the user wants to play the Quiz
#Added '.lower()' to remove the problem of case sensitivity for the answers
#The not equal to sign is used to check for the answer. If the answer is anything but 'yes' then the program will quit itself.
if playing.lower() != "yes":
    quit()
print("Okay, Let's play!")

score = 0

#Notice the lower method is used in the input itself rather than the if condition. This takes the input in the lower case, which helps to use it elsewhere and not limiting the lowercase in the if condition itself.
answer = input("What is the full form of CPU? ").lower()
if answer == "central processing unit":
    print("Congrats, You are correct!")
    score +=1
else:
    print("Incorrect answer.")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Congrats, You are correct!")
    score +=1 #Incrementing the score by 1, each time the user enters a correct answer
else:
    print("Incorrect answer.")

answer = input("What is RAM? ")
if answer.lower() == "random access memory":
    print("Congrats, You are correct!")
    score +=1
else:
    print("Incorrect answer.")

answer = input("What is PSU? ")
if answer.lower() == "power supply":
    print("Congrats, You are correct!")
    score +=1
else:
    print("Incorrect answer.")

#Converted the score variable to string to concatenate it
print("Congrats, You've got " + str(score) + " correct answers!")
print("You've got " + str((score/4)*100) + "%")