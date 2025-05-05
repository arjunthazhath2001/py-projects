from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


window=Tk()
window.title("FLASCARD")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.minsize(900, 800)




canvas= Canvas(width=800,height=526,highlightthickness=0)
front=PhotoImage(file="./images/card_front.png")
canvas.create_image(400,263,image=front)
canvas.config(bg=BACKGROUND_COLOR)
lang_text= canvas.create_text(400,150, text="Title", fill="black",font=("Arial",40,"italic"))
word_text= canvas.create_text(400,290, text="word", fill="black",font=("Arial",60,"bold"))

canvas.grid(row=0,column=0, columnspan=2)



x_img = PhotoImage(file="./images/wrong.png")
x_mark = Button(image=x_img, highlightthickness=0)
x_mark.config(bg=BACKGROUND_COLOR)
x_mark.grid(row=1,column=0,pady=30)


r_img = PhotoImage(file="./images/right.png")
r_mark = Button(image=r_img, highlightthickness=0)
r_mark.config(bg=BACKGROUND_COLOR)
r_mark.grid(row=1,column=1,pady=30)



window.mainloop()