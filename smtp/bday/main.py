import random
import pandas
from datetime import datetime
import smtplib


my_email= "arjunta000@gmail.com"
password="chav mqgd qcvc zons"


data= pandas.read_csv('birthdays.csv')



people=[]
letters=[]
mails=[]

def send_mail(letters):
    for i in range(len(letters)):
        with open(f"{letters[i]}") as file:
            mail= file.read()
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=my_email,password=password)

            connection.sendmail(from_addr=my_email, to_addrs=f"{mails[i]}", msg=f"Subject:HAPPY BIRTHDAY\n\n{mail}")

        
def create_mail(names):  
    letter_number= random.randint(1,3)

    with open(f"./letter_{letter_number}.txt") as file:
        contents= file.read()
        
        
    for i in range(len(names)):
        new_letter= contents.replace('[name]',names[i])
        letters.append(f"./letter_for_{names[i]}.txt")
        with open(f"./letter_for_{names[i]}.txt",'w') as file:
            file.write(new_letter)
    
    send_mail(letters)


for index, row in data.iterrows():
    if row["month"] == datetime.now().month and row["day"] == datetime.now().day:
        people.append(row["name"])
        mails.append(row["email"])            


if people:
    create_mail(people)
            
