import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(my_score,computer_score):
    if my_score == computer_score :
        print('Its a Draw 🙃')
    elif computer_score == 0:
        print('You Lost, Opponent has a BlackJack 😫')
    elif my_score == 0 :
        print('You Won, Its a BlackJack 😲!!!')
    elif computer_score > 21:
        print('You Won, Opponent Went Over😁')
    elif my_score > 21:
        print('You Lost, You Went Over☹️')
    elif my_score > computer_score:
        print('You Won😊')
    else:
        print('You Lost and Opponent Won😧')
    
def play():
    print(logo)
    game = True
    my_cards = []
    computer_cards = []
    u_score = -1
    c_score = -1

    for x in range(2):
        my_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    
    while game:
        u_score = calculate_score(my_cards)
        c_score = calculate_score(computer_cards)

        print(f'Your Cards are {my_cards} and Score is {u_score}')
        print(f"Opponent's First Card is {computer_cards[0]} and Score is **")

        if u_score == 0 or c_score == 0 or u_score > 21:
            game = False
        else:
            deal_one = input('Do you wanna Deal one more Card (Y/N) : ').lower()
            if deal_one == 'y':
                my_cards.append(deal_cards())
            else:
                game = False

    while c_score != 0 and c_score < 17:
        computer_cards.append(deal_cards())
        c_score = calculate_score(computer_cards)

    print(f'Your Final Hand is {my_cards} and Final Score is {u_score}')
    print(f'Your Opponents Final Hand is {computer_cards} and Final score is {c_score}')
    compare(u_score,c_score)

while input('Wanna Play BLACKJACK Game (Y/N) : ').lower() == 'y':
    print('\n'*20)
    play()
