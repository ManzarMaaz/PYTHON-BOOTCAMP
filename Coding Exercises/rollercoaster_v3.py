print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    picture = input('If you want your Ride Picture cost Extra $3 ? (Y/N): ')

    if age <= 12:
        if picture in ("Y",'y'):
            print("Please pay $8 :) ")
        else:
            print("Please pay $5.")
    elif age <= 18:
        if picture in ("Y", 'y'):
            print("Please pay $10 :) ")
        else:
            print("Please pay $7.")
    else:
        if picture in ("Y", 'y'):
            print("Please pay $15 :) ")
        else:
            print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
