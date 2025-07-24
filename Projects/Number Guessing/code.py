import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

HARD_LEVEL_LIVES = 5
EASY_LEVEL_LIVES = 10

def check_guess(guess,answer,choices):
    if guess > answer:
        print('You went High !!!')
        print(f'You have {choices} lives remaining !!!')
        return choices - 1
    elif guess < answer:
        print('You went Low !!!')
        print(f'You have {choices} lives remaining !!!')
        return choices - 1
    else:
        print(f'You Won. The Correct Guess is {guess}')

def difficulty():
    while True:
        level = input('Choose the Difficulty - Easy or Hard : ').lower()
        if level == 'easy':
            return EASY_LEVEL_LIVES
        elif level == 'hard':
            return HARD_LEVEL_LIVES
        else:
            return 'Invalid Input!!!'


def game():
    print(logo)
    print('~~~~~~~~~~~~~~~~~Welcome Number Guessing Game !!!~~~~~~~~~~~~~~')
    print('I think iam a Number between 1-100')
    number = random.randint(1,100)

    turns = difficulty()
    guess = 0
    while guess != number:
        print(f'~~~You have {turns} lives remaining~~~')
        guess = int(input('Guess the Number : '))

        turns = check_guess(guess,number,turns)


        if turns == 0:
            print('Game Over')
            print(f'The Number was {number}')
            return
        elif guess != number:
            print('Try Again !!')

game()
