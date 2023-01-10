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

game_images = [rock, paper, scissors]
user_choice = input("Choose 'Rock', 'Paper' or 'Scissors'")
user_choice = user_choice.lower()

if user_choice == "rock":
  user_choice = 0
elif user_choice == "paper":
  user_choice = 1
elif user_choice == "scissors":
  user_choice = 2
computer_choice = random.randint(0,2)
print(f"You choose {game_images[user_choice]}")
print(f"Computer choose {game_images[computer_choice]}")
if user_choice == 0 and computer_choice == 2:
  print("You won")
elif user_choice == 2 and computer_choice == 0:
  print("Computer won")
elif user_choice > 0 and computer_choice < 1:
  print("You won")
elif user_choice < 0 and computer_choice > 1:
  print("Computer won")
else:
  print("Draw")