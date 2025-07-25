from random import choice
from art import logo, vs
from game_data import data


def display(account):
    account_name = account['name']
    account_work = account['description']
    account_country = account['country']

    return f'{account_name}, A {account_work} from {account_country}'

def compare(choice,a_followers,b_followers):
    if a_followers > b_followers:
        return choice == "a"
    else:
        return choice == "b"

print(logo)
score = 0
game = True
account_b = choice(data)
while game:
    account_a = account_b
    account_b = choice(data)

    if account_a == account_b:
        account_b = choice(data)
    print(f"Compare A : {display(account_a)}")
    print(vs)
    print(f'Against B : {display(account_b)}')

    a_count = account_a['follower_count']
    b_count = account_b['follower_count']

    guess = input('Who has more followers : A or B ? ').lower()
    print('\n'*20)
    print(logo)

    correct = compare(guess,a_count,b_count)

    if correct:
        score += 1
        print(f'You are Right, Score is {score}')
    else:
        print('Oops, Incorrect Answer. Game Over !!!')
        print(f'Final Score is {score}')
        game = False

