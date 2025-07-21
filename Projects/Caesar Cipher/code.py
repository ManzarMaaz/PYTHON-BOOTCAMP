logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

replay = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
    display = ""
    if direction == 'decode':
        shift *= -1
   
    for letter in text:
        if letter not in alphabet:
            display += letter
            continue
    
        old_index = alphabet.index(letter)
        new_index = (old_index + shift)%26
        display += alphabet[new_index]
    

    print(f'The {direction} result is {display}')

while replay:
    ask = input('Select Encode for Encryption and Decode for Decryption : ').lower()
    if ask not in ['encode','decode']:
        print('Invalid Input !!!')
        continue

    message = input('Enter any Message : ')
    shifting = int(input('Enter the Shift Amount : '))
    
    caesar(text=message,shift=shifting,direction=ask)

        

    restart = input('Do you want to Restart (Y/N) : ').lower()

    if restart == 'n':
        replay = False
        print('*********//Game Over//********')
    elif restart == 'y':
        continue
    else:
        print('Invalid Input !!!')
