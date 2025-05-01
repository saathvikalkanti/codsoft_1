# Rock Paper Scissors game.
# Saathvik Alkanti / CodSoft Intern Task 4

import random

user_score = 0
computer_score = 0

while True:
    print("\nChoose rock, paper, or scissors:")
    user = input().lower()

    if user == "rock" or user == "paper" or user == "scissors":
        computer = random.choice(["rock", "paper", "scissors"])
        print("Computer chose:", computer)

        if user == computer:
            print("It's a tie!")
        elif user == "rock" and computer == "scissors":
            print("You win!")
            user_score += 1
        elif user == "paper" and computer == "rock":
            print("You win!")
            user_score += 1
        elif user == "scissors" and computer == "paper":
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print("Score - You:", user_score, "Computer:", computer_score)

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break
    else:
        print("That's not a valid choice. Try again.")
