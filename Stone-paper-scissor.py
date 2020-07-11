
# Program for playing stone paper scissor game.

import random

count_allowed = 0
user_score = 0
computer_score = 0
list = ["s", "p", "c"]

while count_allowed<10:
    print("for stone enter s\nfor paper enter p\nfor scissor enter c\n")
    user_actual_input = input("Enter choice:\n")
    user_input = user_actual_input.lower()
    computer_input = random.choice(list)
    print(computer_input)
    if  user_input == computer_input:
        print("There is a tie and you both get one point")
        user_score+=1
        computer_score+=1
        print(f"Your score is {user_score} and computer's score is {computer_score}")
    elif user_input == "s" and computer_input == "c":
        print("Your stone crushed the computer's scissor")
        user_score+=1
        print(f"Your score is {user_score} and computer's score is {computer_score}")
    elif user_input == "s" and computer_input == "p":
        print("Computer's paper revoked your stone")
        computer_score+=1
        print(f"Your score is {user_score} and computer's score is {computer_score}")
    elif user_input == "p" and computer_input == "s":
        print("Your paper revoked computer's stone")
        user_score+=1
        print(f"Your score is {user_score} and computer's score is {computer_score}")
    elif user_input == "p" and computer_input == "c":
        print("Computer's scissor cut your paper")
        computer_score+=1
        print(f"Your score is {user_score} and computer's score is {computer_score}")
    elif user_input == "c" and computer_input == "s":
        print("Your scissor was crushed by computer's stone")
        computer_score+=1
        print(f"Your score is {user_score} and computer's score is {computer_score}")
    elif user_input == "c" and computer_input == "p" :
        print("You cut computer's paper")
        user_score+=1
        print(f"Your score is {user_score} and computer's score is {computer_score}")
    else:
        print("You need to enter a correct value")
        count_allowed = 9

    count_allowed+=1
    print(f"Now, allowed trials are {10 - count_allowed} \n")

print("Game Over!")

print(f"Your final score is {user_score} and computer's final score is {computer_score}")

if user_score>computer_score:
    print("Congratulations, You Won!\n \n")
elif user_score<computer_score:
    print("You lose and computer won!\n \n")
elif user_score == 0 and computer_score == 0:
    print("Try again!")
else:
    print("Well, there is a tie!")