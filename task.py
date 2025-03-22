import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#list
game = [rock,paper,scissors]
#turn user choice to integer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#randomize computer choice from the list
computer_choice = random.choice(game)

print(game[user_choice])
print("computer choose:")
print(computer_choice)

#if condition for the game
if user_choice == 0 and computer_choice == paper:
    print("You Lose")
elif user_choice == 0 and computer_choice == scissors:
    print("You Win")
elif user_choice == 1 and computer_choice == rock:
    print("You Win")
elif user_choice == 1 and computer_choice == scissors:
    print("You Lose")
elif user_choice == 2 and computer_choice == rock:
    print("You Lose")
elif user_choice == 2 and computer_choice == paper:
    print("You win")
else:
    print("It's a draw")