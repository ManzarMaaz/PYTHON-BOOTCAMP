import random
from random import randint

print("********** WELCOME TO ROCK, PAPER AND SCISSORS GAME **********")

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
images = [rock,paper,scissors]
images_names = ['Rock','Paper','Scissors']
my_choice = int(input('Choose 0 for Rock, 1 for Paper or 2 for Scissors ?\n'))
if my_choice not in (0,1,2):
    print('Invalid Input !!!')

else:
    print(f'You Chose : {images_names[my_choice]}\n',images[my_choice])
    computer = randint(0, 2)
    print(f'Your Opponent chose : {images_names[computer]}\n', images[computer])

    if (my_choice == 1 and computer == 2) or (my_choice == 3 and computer == 2) or (my_choice == 2 and computer == 1):
        print(f'You Wins !!!')
    elif my_choice == computer:
        print('Its a Draw !!!')
    else:
        print(f'You Lost !!!')

