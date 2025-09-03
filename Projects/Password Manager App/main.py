from tkinter import *
from tkinter import messagebox
from random import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    easy_password = ''

    for x in range(0,4):
        random_letters = choice(letters)
        easy_password += random_letters

    for y in range(0,2):
        random_symbols = choice(symbols)
        easy_password += random_symbols

    for z in range(0,2):
        random_numbers = choice(numbers)
        easy_password += random_numbers

    pass_list = list(easy_password)
    shuffle(pass_list)
    hard_password = "".join(pass_list)
    
    password_entry.insert(0,hard_password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_entry.get()
    username = name_entry.get()
    password = password_entry.get()


    if website == "" or username == "" or password == "":
        messagebox.showwarning(title='Invalid Info', message='The required Fields are Empty')

    else:    
        fill = messagebox.askokcancel(title=website, message=f"Do you want to Proceed with this Info: \nWebsite: {website} \nID: {username} \nPassword: {password}")
        
        if fill:
            with open('Saved_Passwords.txt',mode='a') as file:
                file.write(f"{website} |  {username} | {password} \n")

                website_entry.delete(0,END)
                name_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Py Password Manager')
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
canvas.grid(row=0, column=1)

photo = PhotoImage(file='./DAY 29/password-manager-start/logo.png')

logo = canvas.create_image(100,90, image=photo)


website = Label(text='Website Name :')
website.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()

name = Label(text='Username/Mail :')
name.grid(row=2, column=0)

name_entry = Entry(width=35)
name_entry.grid(row=2,column=1, columnspan=2)

password = Label(text='Password :')
password.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate = Button(text='Generate', width=10, command=pass_generator)
generate.grid(row=3, column=2)

save = Button(text='Save',command=save_password, width=33)
save.grid(row=4, column=1, columnspan=2)




window.mainloop()