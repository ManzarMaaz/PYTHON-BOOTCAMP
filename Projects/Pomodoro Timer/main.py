
# ---------------------------- CONSTANTS ------------------------------- #
import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
job = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    window.after_cancel(job)
    canvas.itemconfig(timer_text, text='00:00')
    check.config(text='')
    timer_label.config(text='Timer')
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global reps
    reps += 1

    if reps%8 == 0: #Long Break
        counter(LONG_BREAK_MIN*60)
        timer_label.config(text='LONG BREAK', fg='RED')

    elif reps%2 == 0: #Short Breaks
        counter(SHORT_BREAK_MIN*60)
        timer_label.config(text='SHORT BREAK', fg=PINK)

    elif reps%2 != 0: #Normal Rounds
        counter(WORK_MIN*60)
        timer_label.config(text='WORK TIME', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    global reps

    minutes = math.floor(count/60)
    seconds = count % 60
        
    if seconds == 0 or seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text= f'{minutes}:{seconds}')
    
    if count > 0:
        global job
        job = canvas.after(1000, counter, count - 1)
    else:
        timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✅'
        check.config(text=marks)

    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro Counter')
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightbackground=YELLOW)

photo = PhotoImage(file='./DAY 28/pomodoro-start/tomato.png')

timer_label = Label(text='Timer', fg=GREEN ,font=(FONT_NAME, 25, 'bold'), bg=YELLOW)
timer_label.grid(row=0 , column=1)

tomato_image = canvas.create_image(103,112, image=photo)

timer_text = canvas.create_text(100,125,text='00:00', font=(FONT_NAME, 35, 'bold'))

canvas.grid(row=1,column=1)

check = Label(bg=YELLOW)
check.grid(row=3 , column=1)

start = Button(text='Start', command=timer, highlightbackground=YELLOW)
start.grid(row=2,column=0)

reset = Button(text='Reset', command=timer_reset,highlightbackground=YELLOW)
reset.grid(row=2,column=2)


window.mainloop()