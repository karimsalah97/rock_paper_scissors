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

#Write your code below this line 👇
import random
#creating the list
game = [rock, paper, scissors]
#creat an input for the user
user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
if user == "0":
  print(rock)
elif user == "1":
  print(paper)
else :
  print(scissors)

print("Computer choose:")
# randomization of the game
pc = random.choice(game)
print(pc)
# if condition for the game
if user == "0" and pc == scissors:
  print("You win")
elif user == "0" and pc == paper:
  print("You Lose")
elif user == "1" and pc == scissors:
  print("You Lose")
elif user == "1" and pc == rock:
  print("You Win")
elif user == "2" and pc == rock:
  print("You Lose")
elif user == "2" and pc == paper:
  print("You Win")
else :
  print("Draw")