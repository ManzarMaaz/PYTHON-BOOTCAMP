logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}

def calculator():
    calculation = True
    num1 = int(input('Choose any Integer : '))
    while calculation:
        for symbols in operations:
            print(symbols)
        select = input('Choose the Method : ')
        num2 = int(input('Choose another Integer : '))
        if select in ['+', '-', '*', '/']:
            result = operations[select](num1, num2)
            print(f'{num1} {select} {num2} = {result}')
        else:
            print('Invalid Method Selected!!!')

        restart = input("Do you want to Exit (Y/N) : ").lower()
        if restart == 'n':
            replay = input(f'Do you want to continue with the Present Result {result} (Y/N) : ').lower()
            if replay == "y":
                num1 = result
            elif replay == 'n':
                result = 0
                print('\n' * 10)
                calculator()
            else:
                print("invalid Input")
        else:
            calculation = False
            break



calculator()
