from random import choice
word_list = [
    "apple", "ball", "cat", "dog", "egg",
    "fish", "goat", "hat", "ice", "jam",
    "kite", "lion", "milk", "nose", "owl",
    "pen", "queen", "rat", "sun", "tree",
    "van", "water", "xray", "yak", "zebra"
]
chosen_word = choice(word_list)

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
print(chosen_word)
placeholder = ""

for letter in range(len(chosen_word)):
    placeholder += '_'
print("Word to Guess : " + placeholder)

game_on = True
lives = 6
correct_letters = []

while game_on:
    print(f'******************{lives}/6 Lives Left***********************')
    guess = input('Choose a Letter : ').lower()

    if guess in correct_letters:
        print(f'You have Already Guessed {guess}')
    
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"
    
    print('Word to guess: ' + display)

    if '_' not in display:
        print("**********You Won !!!**********")
        game_on = False

    if guess not in chosen_word:
        lives -= 1
        print('Incorrect Guess')
        print(f'You lost a Life\nRemaining {lives} lives !!!')
    
        if lives == 0:
            game_on = False
            print(f'The Correct word was {chosen_word}\n'
                  '***********You Lost!!!************')

    print(stages[lives])
