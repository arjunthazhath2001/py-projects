from tkinter import *

window= Tk()

window.minsize(width=300, height=200)

window.title("MILE TO KM CONVERTER")
window.configure(background="white")
window.configure(padx=20,pady=20)


########3######### ROW 1 #########################

my_label= Label(text="Miles")
my_label.configure(background="white")
my_label.grid(row=0, column=2, padx=5, pady=5)


#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="0")
entry.grid(row=0, column=1, padx=5, pady=5)



############### ROW 2 ###########################

new_label1= Label(text="is equal to")
new_label1.configure(background="white")
new_label1.grid(row=1, column=0, padx=5, pady=5)


new_label2= Label(text="0")
new_label2.configure(background="white")
new_label2.grid(row=1, column=1, padx=5, pady=5)


new_label3= Label(text="Km")
new_label3.configure(background="white")
new_label3.grid(row=1, column=2, padx=5, pady=5)

#################################################

def action():
    mile= float(entry.get())
    km= mile*1.609
    new_label2.config(text=f"{km}")

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=2, column=1, padx=5, pady=5)



window.mainloop()