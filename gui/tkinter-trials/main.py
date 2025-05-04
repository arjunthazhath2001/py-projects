import tkinter

window= tkinter.Tk()

window.minsize(width=500, height=300)

window.title("my gui")

my_label= tkinter.Label(text="you are awesome", font=("Arial",18,"bold"))

my_label.pack(side="right")

# my_label.pack(side="bottom")

my_label["text"]="arjun is awesome"
my_label.config(text="arjun is great")





window.mainloop()