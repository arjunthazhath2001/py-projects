from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR= "#375362"

class QuizInterface:
    
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz= quiz_brain
        self.window=Tk()
        self.window.title("quiz")
        self.window.minsize(width=500,height=600)
        self.window.configure(bg=THEME_COLOR,padx=10,pady=60)
        
        self.score_label= Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.config(font=("Arial",30,"bold"))
        self.score_label.grid(row=0,column=2)
        
        self.canvas = Canvas(width=400, height=400, bg="white")
        self.question_text= self.canvas.create_text(200,200, width=300,text="Some qustions",font=("Arial",20,'normal'))
        self.canvas.grid(row=1, column=0, columnspan=3, padx=30, pady=20)


        right_img = PhotoImage(file="right.png")
        right_img = right_img.subsample(8, 8)  
        self.right_button = Button(image=right_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        
        wrong_img = PhotoImage(file="wrong.png")
        wrong_img = wrong_img.subsample(5, 5)  
        self.wrong_button = Button(image=wrong_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.config(padx=20,pady=20)
        
        self.wrong_button.grid(row=2, column=0, padx=20, pady=20)
        self.right_button.grid(row=2, column=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)
    
    def true_pressed(self):
        self.get_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        self.get_feedback(self.quiz.check_answer("False"))

    
    def get_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")