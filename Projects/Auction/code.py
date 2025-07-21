logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print('**********//Welcome to the Auction//**********')

replay = True

def winner(auction):
    max_bid = 0
    winner_name = ""

    for bidder, bid_amount in auction.items():
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner_name = bidder

    print(f'The Winner is {winner_name} with ${max_bid}')

    
bidding = {}

while replay:

    name = input('Enter your Name : ').capitalize()
    bids = int(input('Enter the Bidding Amount : $'))

    bidding[name] = bids 

    restart = input('Aby other Bids (Y/N) : ').lower()

    if restart == 'n':
        replay = False
        winner(bidding)
    elif restart == 'y':
        print('\n'*20)
    else:
        print('Invalid Input !!!')
        continue



