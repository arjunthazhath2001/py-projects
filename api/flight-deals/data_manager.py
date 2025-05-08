import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

AUTH_HEADER=os.getenv('AUTH_HEADER')



SHEETY_URL="https://api.sheety.co/f97511de9beacb5be16d261bede9f763/flightDeals/prices"

headers = {
    "Content-Type": "application/json",
    "Authorization": AUTH_HEADER
}



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):    
        self.response= requests.get(url=SHEETY_URL,headers=headers)
        
    
    def update(self,data):
        PUT_URL= f"{SHEETY_URL}/{data['id']}"
        
        sheet_params={
        "price" :{

            "iataCode": data['iataCode']            
        }
    }
        res=requests.put(url=PUT_URL, json=sheet_params,headers=headers)
        print(res.text)