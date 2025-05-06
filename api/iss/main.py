import requests
import datetime as dt

MY_LAT=51.507351
MY_LONG=-0.127758


response= requests.get()







parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}



response= requests.get("https://api.sunrise-sunset.org/json",params=parameters)

sunrise= response.json()["results"]["sunrise"].split("T")[1].split(':')[0]
sunset= response.json()["results"]["sunset"].split("T")[1].split(':')[0]

print(sunrise)
print(sunset)
time_now= dt.datetime.now()


print(time_now)