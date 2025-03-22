import random

# ASCII Art
rock = "Rock ✊"
paper = "Paper ✋"
scissors = "Scissors ✌️"

# List of choices
game = [rock, paper, scissors]

# Get user choice
user_choice = int(input("Choose: 0 for Rock, 1 for Paper, 2 for Scissors: "))

# Validate input
if user_choice not in [0, 1, 2]:
    print("Invalid choice! Please choose 0, 1, or 2.")
else:
    # Get computer choice (as an index)
    computer_choice = random.randint(0, 2)

    # Display choices
    print(f"\nYou chose: {game[user_choice]}")
    print(f"Computer chose: {game[computer_choice]}")

    # Game logic
    if user_choice == computer_choice:
        print("It's a draw! 🤝")
    elif (user_choice, computer_choice) in [(0, 2), (1, 0), (2, 1)]:
        print("You win! 🎉")
    else:
        print("You lose! 😢")
