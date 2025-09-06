from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    file_csv = pandas.read_csv('DAY 31/flash-card-project-start/data_arabic/remaining_arabic.csv')
except:
    file_csv = pandas.read_csv('DAY 31/flash-card-project-start/data_arabic/quran_100_full.csv')

data_dict = file_csv.to_dict(orient='records')

flip_card = None

random_row = {}

def flip():
    canvas.itemconfig(card, image=back_image)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=random_row['English'].title(), fill='white')
    canvas.itemconfig(transliteration, text='')
    canvas.itemconfig(frequency, text=f"Frequency: {random_row['Frequency']}", fill='white')
    canvas.itemconfig(parts_of_speech, text=f"P.O.S: {random_row['POS'].title()}", fill='white')

def next_card():
    global random_row, flip_card

    if flip_card is not None:
        window.after_cancel(flip_card)

    random_row = random.choice(data_dict)

    canvas.itemconfig(card, image=front_image)
    canvas.itemconfig(title, text='Arabic', fill='black')
    canvas.itemconfig(word, text=random_row['Arabic'], fill='black')
    canvas.itemconfig(transliteration, text=random_row['Transliteration'], fill='black')
    canvas.itemconfig(frequency, text=f"Frequency: {random_row['Frequency']}", fill='black')
    canvas.itemconfig(parts_of_speech, text=f"P.O.S: {random_row['POS'].title()}", fill='black')

    flip_card = window.after(3000, flip)

def remove_known_card():
    data_dict.remove(random_row)
    data = pandas.DataFrame(data_dict)
    data.to_csv('DAY 31/flash-card-project-start/data_arabic/remaining_arabic.csv', index=False)
    next_card()

    


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# flip_card = window.after(3000, flip)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

front_image = PhotoImage(file="DAY 31/flash-card-project-start/images/card_front.png")
back_image = PhotoImage(file="DAY 31/flash-card-project-start/images/card_back.png")

right_image = PhotoImage(file="DAY 31/flash-card-project-start/images/right.png")
wrong_image = PhotoImage(file="DAY 31/flash-card-project-start/images/wrong.png")

card = canvas.create_image(400,263, image=front_image)

title = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'), fill='black')
word = canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'), fill='black')
transliteration = canvas.create_text(400, 350, text='Transliteration', font=('Arial', 25, 'bold'), fill='black')
parts_of_speech = canvas.create_text(600, 450, text='Parts of Speech', font=('Arial', 15, 'italic'), fill='black')
frequency = canvas.create_text(200, 450, text='Frequency', font=('Arial', 15, 'italic'), fill='black')


right_button = Button(image=right_image, command=remove_known_card, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, command=next_card, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
