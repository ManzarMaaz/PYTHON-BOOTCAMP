MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

income = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_availability(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f'Sorry, There is not Enough {item}')
            return False
    return True

def counter():
    print('Please Insert Money: ')
    total = float(input('Enter Quarters : '))*0.25
    total += float(input('Enter Dimes : '))*0.10
    total += float(input('Enter Nickles : '))*0.05
    total += float(input('Enter Pennies : '))*0.01
    return total

def payment_succesful(paid, price):
    global income
    if paid < price:
        print('Not Enough Money')
        print('Your Money Refunded')
        return False
    else:
        income += price
        change = round(paid - price, 2)
        print(f'You given an amount of ${paid}')
        print(f"The Cost of {user_input} is ${price}")
        print(f'Here is your change of ${change}')
        return True

def coffee_maker(order, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f'Here is your Fresh {order} 🥤☕️ !!!')

machine = True

while machine:
    user_input = input('What would you like? (Espresso, Latte, Cappuccino) :').lower()

    if user_input == 'off':
        machine = False
    elif user_input == "report":
        print(f'Water : {resources["water"]}ml\n'
              f'Milk : {resources["milk"]}ml\n'
              f'Coffee : {resources["coffee"]}g\n'
              f'Money : ${income}')
    else:
        drink = MENU[user_input]
        drink_ingredients = drink['ingredients']
        drink_cost = drink['cost']
        if resource_availability(drink_ingredients):
            dollars = counter()
            if payment_succesful(paid=dollars, price=drink_cost):
                coffee_maker(user_input, drink_ingredients)
