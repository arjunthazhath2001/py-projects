import requests
import datetime as dt
import smtplib

MY_LAT=51.507351
MY_LONG=-0.127758

my_email= "arjunta000@gmail.com"
password="chav mqgd qcvc zons"

def within_range():

    response= requests.get(url="http://api.open-notify.org/iss-now.json")
    data=response.json()

    iss_latitude= float(data["iss_position"]["latitude"])
    iss_longitude= float(data["iss_position"]["longitude"])
    print(iss_latitude)
    print(iss_longitude)

    if ((MY_LAT-5)<=iss_latitude<=(MY_LAT+5)) and ((MY_LONG-5)<=iss_longitude<=(MY_LONG+5)):
        return True
    else:
        False
        


def is_night():
    parameters={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }



    response= requests.get("https://api.sunrise-sunset.org/json",params=parameters)

    sunrise= int(response.json()["results"]["sunrise"].split("T")[1].split(':')[0])
    sunset= int(response.json()["results"]["sunset"].split("T")[1].split(':')[0])

    print(sunrise)
    print(sunset)
    time_now= dt.datetime.now().hour

    if sunset<=time_now<=sunrise:
        return True




if is_night() and within_range():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email,password=password)

        connection.sendmail(from_addr=my_email, to_addrs="arjunta000@gmail.com", msg=f"Subject:ISS\n\nLOOKUP")
else:
    print("False")

    
    
