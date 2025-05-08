import requests
import os
from dotenv import load_dotenv

load_dotenv()


from twilio.rest import Client

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')



params={
    "lat":11.010048,
    "lon":76.9523712,
    "appid": os.environ.get('API_KEY'),
    "cnt":4
}

response= requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=params)

response.raise_for_status()
weather_data=response.json()

res=[]

weather_list= weather_data["list"]

for i in range(len(weather_list)):
    weather_id=weather_list[i]['weather'][0]['id']
    if(weather_id)<700:
        res.append(weather_id)


if res:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="TAKE UMBRELLA BRO",
    from_="whatsapp:+14155238886",
    to="whatsapp:+918838630198",
    )

else:
    print("no umbrella")

