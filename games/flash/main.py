from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

current_card={}

try:
    data= pandas.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    original_data= pandas.read_csv("./data/french_words.csv")
    list_data= original_data.to_dict(orient="records")
else:
    list_data= data.to_dict(orient="records")

flip_timer= None


def flip():
    canvas.itemconfig(canvas_image, image=new_image)
    
    canvas.itemconfig(lang_text,fill="white",text="English")
    canvas.itemconfig(word_text,fill="white",text=current_card["English"])



def generate_word():
    global flip_timer,current_card
    if flip_timer:
        window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=old)
    
    current_card= random.choice(list_data)    
 
    canvas.itemconfig(lang_text,fill="black",text="French")
    canvas.itemconfig(word_text,fill="black",text=current_card["French"])
    flip_timer=window.after(3000,flip)


def is_known():
    list_data.remove(current_card)
    print(len(list_data))
    data=pandas.DataFrame(list_data)
    data.to_csv("./data/to_learn.csv",index=False)
    generate_word()
    



window=Tk()
window.title("FLASCARD")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.minsize(900, 800)


canvas= Canvas(width=800,height=526,highlightthickness=0)


new_image= PhotoImage(file="./images/card_back.png")
old=PhotoImage(file="./images/card_front.png")
canvas_image=canvas.create_image(400,263,image=old)
canvas.config(bg=BACKGROUND_COLOR)


lang_text= canvas.create_text(400,150, text="", fill="black",font=("Arial",40,"italic"))
word_text= canvas.create_text(400,290, text="", fill="black",font=("Arial",60,"bold"))

canvas.grid(row=0,column=0, columnspan=2)



x_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=x_img, highlightthickness=0,command=generate_word)
unknown_button.config(bg=BACKGROUND_COLOR)
unknown_button.grid(row=1,column=0,pady=30)


r_img = PhotoImage(file="./images/right.png")
known_button= Button(image=r_img, highlightthickness=0,command=is_known)
known_button.config(bg=BACKGROUND_COLOR)
known_button.grid(row=1,column=1,pady=30)

generate_word()


window.mainloop()