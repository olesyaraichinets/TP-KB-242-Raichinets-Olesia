import random

options = ["stone", "scissor", "paper"]
user_choice = input("Enter stone, scissor або paper: ").lower()

if user_choice not in options:
    print("Wrong choice!")
else:
    computer_choice = random.choice(options)
    print(f"Computer selection: {computer_choice}")

    if user_choice == computer_choice:
        print("Draw!")
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        print("You win!")
    else:
        print("You lost!")
