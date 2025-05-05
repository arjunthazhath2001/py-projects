import smtplib
import datetime as dt
import random

my_email= "arjunta000@gmail.com"
password="chav mqgd qcvc zons"


with open("quotes.txt") as file:
    quotes= file.readlines()
    quote=random.choice(quotes)

now= dt.datetime.now()
day_of_week= now.weekday()


if day_of_week==0:
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email,password=password)

        connection.sendmail(from_addr=my_email, to_addrs="arjunta32@gmail.com", msg="Subject:hey\n\nTHIS IS BODY")




    