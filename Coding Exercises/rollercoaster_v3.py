print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 12:
        bill = 5
        print("Child Tickets are $5.")

    elif age <= 18:
        bill = 7
        print("Youth Tickets are $7.")

    else:
        bill = 12
        print("Adult Tickets are $12.")

    picture = input('If you want your Ride Picture, It costs Extra $3 ? (Y/N): ')
    if picture in ('Y','y'):
        bill += 3
    print(f'Your Final Bill is ${bill}')

else:
    print("Sorry you have to grow taller before you can ride.")
