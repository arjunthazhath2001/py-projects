from tkinter import *
import random
from more_itertools import random_permutation
from tkinter import messagebox
import clipboard as cp
import json
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------------------------------------------------- #



def popup():
    website= entry.get()
    email= entry2.get()
    passwd= entry3.get()
    new_data={
        website:{
            'email':email,
            'password':passwd
        }
    }
    
    if len(website)==0:
        messagebox.showerror("Error","Website name should atleast have 1 char")
        return 
    elif len(email)==0:
        messagebox.showerror("Error","Enter valid email")
        return 
    
    elif len(passwd)==0:
        messagebox.showerror("Error","Pls enter pswd")
        return

    else:
    
        is_ok= messagebox.askokcancel(title=website,message=f"{email}:{passwd} is this ok?")
        
        if is_ok:
            try:
                with open("data.json",'r') as file:
                    data=json.load(file)
            except FileNotFoundError:
                with open("data.json","w") as file:
                    json.dump(new_data,file,indent=4)
            else:
                data.update(new_data)
                with open("data.json","w") as file:
                    json.dump(data,file,indent=4)
            finally:
                entry.delete(0,END)
                entry2.delete(0,END)
                entry3.delete(0,END)


    

def gen_password():
    alphabet = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    numbers = [str(i) for i in range(10)]
    special_chars = list("!@#$%^&*()=+[]{}|;:<>?/")
    al=""
    for i in range(3):
        al+= random.choice(alphabet)
    for i in range(3):
        al+= random.choice(numbers)
    for i in range(2):
        al+=random.choice(special_chars)
    
    entry3.delete(0, END)
    al= ''.join(random_permutation(al))
    entry3.insert(0,al)
    cp.copy(al)


def search():
    website= entry.get()

    try:
        with open("data.json",'r') as file:
            data=json.load(file)
        email= data[website]['email']
        password= data[website]['password']
    
    except FileNotFoundError:
        messagebox.showerror("Error","FIle Doesnot exist")
    except KeyError:
        messagebox.showerror("Error","WEBSITE Doesnot exist")
    else:
        messagebox.askokcancel(title=website,message=f"Email={email}\nPassword:{password}")
    

window=Tk()
window.title("PASSWORD MANAGER")
window.config(padx=60,pady=60,bg="white")
window.minsize(width=600, height=500)




canvas= Canvas(width=200,height=224,bg="white",highlightthickness=0)
tom=PhotoImage(file="logo.png")
canvas.create_image(100,112,image=tom)
canvas.grid(row=0,column=1)


# ---------------------------------------------------------------------- #

label1= Label(text="Website:")
label1.configure(background="white")
label1.grid(row=1, column=0, padx=5, pady=5)

#Entries
entry = Entry(width=30)
entry.focus()
entry.grid(row=1, column=1, padx=5, pady=5)

button3 = Button(text="Search",fg="white",width=20,bg="blue",highlightthickness=0,command=search)
button3.grid(row=1, column=2, padx=5, pady=5)


# ---------------------------------------------------------------------- #


label2= Label(text="Email/Username:")
label2.configure(background="white")
label2.grid(row=2, column=0, padx=5, pady=5)


#Entries
entry2 = Entry(width=30)
entry2.grid(row=2, column=1, padx=5, pady=5)

# ---------------------------------------------------------------------- #

label3= Label(text="Password:")
label3.configure(background="white")
label3.grid(row=3, column=0, padx=5, pady=5)


#Entries
entry3 = Entry(width=30)
entry3.grid(row=3, column=1,pady=5)



button1 = Button(text="Generate password",bg="white",highlightthickness=0,command=gen_password)
button1.grid(row=3, column=2, padx=5, pady=5)

button2 = Button(text="Add password",bg="white",width=30,highlightthickness=0, command=popup)
button2.grid(row=4, column=1, padx=5, pady=5)


window.mainloop()