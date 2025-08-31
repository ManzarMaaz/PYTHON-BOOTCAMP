from tkinter import *

# Create main window
window = Tk()
window.title('Kilometers to Miles Converter')
window.minsize(300, 150)

# Label for input
my_label = Label(text='Kilometers')
my_label.pack()

# Entry box
input_box = Entry(width=15)
input_box.pack()

# Result label (empty at first)
result_label = Label(text="Result will appear here")
result_label.pack()

# Function to calculate miles
def result():
    try:
        km = float(input_box.get())  # allow decimal input
        miles = km * 0.621371        # more accurate conversion factor
        result_label.config(text=f"= {miles:.2f} Miles")  # update label
    except ValueError:
        result_label.config(text="Please enter a number")

# Button
click_here = Button(text='Calculate', command=result)
click_here.pack()

# Run the window
window.mainloop()
