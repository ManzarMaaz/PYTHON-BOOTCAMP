from coffee_maker import CoffeeMaker 
from money_machine import MoneyMachine
from menu import Menu

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
valid_options = ['cappuccino','espresso','latte','report','off']



start_machine = True

while start_machine:
    choice = input('Choose any Drink (Cappuccino, Espresso, Latte) : ').lower()

    if choice not in valid_options:
        print('Invalid Choice !! Try Again.')
    else:
        if choice == 'off':
            start_machine = False
            print('The Machine is Switched Off')
        elif choice == 'report':
            print('The Current Report of the Machine is :')
            coffee_maker.report()
            money_machine.report()
        else:
            my_drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(my_drink):
                if money_machine.make_payment(my_drink.cost):
                    coffee_maker.make_coffee(my_drink)
                    