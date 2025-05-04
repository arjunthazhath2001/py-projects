from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    pomo_number.config(text="")
    my_label.config(text="Timer")
    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec= WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break_sec= LONG_BREAK_MIN*60
    
    if reps%2==1:
        my_label.configure(text="WORK")
        count_down(work_sec)
        
    elif reps%8==0:
        my_label.configure(text="LONG BREAK",fg=RED)
        count_down(long_break_sec)
        
    else:
        my_label.configure(text="SHORT BREAK",fg=PINK)
        count_down(short_break_sec)
        

        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    if count=="stop":
        return 
    count_min= math.floor(count/60)
    count_sec= int(count%60)
    
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        
        for i in range(math.floor(reps/2)):
            marks+="✅"
        pomo_number.config(text=marks)
        
         

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("POMODORO")
window.config(padx=100,pady=100,bg=YELLOW)


my_label= Label(text="Timer",font=(FONT_NAME,55,"bold"))
my_label.configure(fg=GREEN,bg=YELLOW)
my_label.grid(row=0, column=1)



canvas= Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tom=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tom)
timer_text= canvas.create_text(103,130, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)




button1 = Button(text="Start",bg="white",highlightthickness=0, command=start_timer)
button1.grid(row=2, column=0, padx=5, pady=5)


button2= Button(text="Reset",bg="white",highlightthickness=0, command=reset_timer)
button2.grid(row=2, column=2, padx=5, pady=5)


pomo_number = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
pomo_number.grid(row=3, column=1)




window.mainloop()