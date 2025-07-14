print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size in ('S', "s"):
    bill += 15
elif size in ('M', 'm'):
    bill += 20
elif size in ('L','l'):
    bill += 25
else:
    print('Invalid Input !!!')

if pepperoni in ('Y','y'):
    print('Added Pepperoni !!')
    if size in ('S',"s"):
        bill += 2
    elif size in ('M','m','l','L'):
        bill += 3

if extra_cheese in ('Y','y'):
    print('Added Extra Cheese !!')
    bill += 1

print(f'Your final bill is: ${bill}.')
