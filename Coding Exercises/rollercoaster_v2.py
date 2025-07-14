print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("May i know your Age in Years : "))

    if age <= 12:
        print('Your Ticket price is $5')
    elif 12 < age < 18:
        print('Your Ticket price is $7')
    elif age >= 18:
        print('Your Ticket price is $12')
else:
    print("Sorry you have to grow taller before you can ride.")
