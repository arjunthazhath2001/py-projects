#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


from data_manager import DataManager
from flight_search import FlightSearch


data_manager= DataManager()


list_data= data_manager.response.json()['prices']

for data in list_data:
    flight_search= FlightSearch(data)
    data['iataCode']= flight_search.city['iataCode']


for data in list_data:
    data_manager.update(data)
    # print(data)
