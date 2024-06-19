import random

hands = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

user_input = input("(Rock, Paper, Scissors, Lizard or Spock) What do you choose?: ")

user_choice = user_input.lower()
computer_choice = random.choice(list(hands.keys()))


def winner(user_choice, computer_choice):
    if computer_choice == user_choice:
        return f"Computer chose {computer_choice}, It's a tie!"

    else:
        for key, value in hands.items():
            if computer_choice in value:
                if user_choice == key:
                    return f"Computer chose {computer_choice}, you won!"
                else:
                    return f"Computer chose {computer_choice}, you lost."


print(winner(user_choice, computer_choice))
