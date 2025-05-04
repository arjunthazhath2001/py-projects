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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min= math.floor(count/60)
    count_sec= count%60
    
    if count_sec==0:
        count_sec="00"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_down,count-1)

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


button2= Button(text="Reset",bg="white",highlightthickness=0)
button2.grid(row=2, column=2, padx=5, pady=5)


pomo_number = Label(text="✅", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
pomo_number.grid(row=3, column=1)




window.mainloop()