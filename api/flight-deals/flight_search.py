import os
from dotenv import load_dotenv
import requests
import datetime as dt


load_dotenv()



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.API_KEY=os.getenv('API_KEY')
        self.API_SECRET=os.getenv('API_SECRET')
        self.token= self.get_new_token()
        print(self.token)
        
        
    
    def get_iat(self,city):
        city_search_url="https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers={
            "Authorization": f"Bearer {self.token}"
        }
        params={
            "keyword": city['city'],
            "max":"1"
        }
        
        response= requests.get(url=city_search_url,params=params,headers=headers)
        self.city=city
        self.city['iataCode']=response.json()['data'][0]['iataCode']
        
    
    def get_new_token(self):
        token_request_url="https://test.api.amadeus.com/v1/security/oauth2/token"
        token_headers={
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        params={
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET
        }
        
        response= requests.post(url=token_request_url,data=params,headers=token_headers)
        return response.json()["access_token"]
    
    
    def get_prices(self,city):
        price_request_url= "https://test.api.amadeus.com/v2/shopping/flight-offers"
        
        self.city=city
        date= dt.datetime.now().strftime('%Y-%m-%d')
        headers={
            "Authorization": f"Bearer {self.token}"
        }
        params={
            "originLocationCode": "LON",
            "destinationLocationCode": self.city['iataCode'],
            "departureDate": date,
            "adults": 1,
            "nonStop": "true",
        }
        
        response= requests.get(url=price_request_url,params=params,headers=headers)
        print(response.text)

    
    