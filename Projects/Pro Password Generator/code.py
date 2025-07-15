import random
from random import choice
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("~~~~~~~~~~ Welcome to the ProPyPassword Generator! ~~~~~~~~~~")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

easy_password = ''

for x in range(0,nr_letters):
    random_letters = choice(letters)
    easy_password += random_letters

for y in range(0,nr_symbols):
    random_symbols = choice(symbols)
    easy_password += random_symbols

for z in range(0,nr_numbers):
    random_numbers = choice(numbers)
    easy_password += random_numbers

print(list(easy_password))
print("Pattern Version : ",easy_password,'\n')

pass_list = list(easy_password)
random.shuffle(pass_list)
print(pass_list)

hard_password = "".join(pass_list)
print('Shuffled Version : ',hard_password)
