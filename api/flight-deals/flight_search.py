class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,city):
        self.city= city
        self.city['iataCode']='NEW_TESTING'
                