from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=30, pady=50, bg=THEME_COLOR)

        self.score_text = Label(text=f'Score: 0', fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=330, 
                             background='white', 
                             highlightthickness=0)
        
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)


        self.question_text = self.canvas.create_text(165,125, 
                                                     width=310,
                                                     text='Question comes here...', 
                                                     fill='black', 
                                                     font=("Arial", 20, "italic"),
                                                     anchor="center")
        

        self.true_logo = PhotoImage(file="DAY 34/quizzler-app-start/images/true.png")
        self.false_logo = PhotoImage(file="DAY 34/quizzler-app-start/images/false.png")

        self.true_button = Button(image=self.true_logo, 
                                  highlightthickness=0, 
                                  highlightbackground=THEME_COLOR,
                                  command=self.true_pressed)
        
        self.false_button = Button(image=self.false_logo, 
                                   highlightthickness=0, 
                                   highlightbackground=THEME_COLOR,
                                   command=self.false_pressed)

        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg='white')
            self.score_text.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.config(bg="white")
        
    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000,self.get_next_question)
