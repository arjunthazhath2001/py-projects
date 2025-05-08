import requests
import os
from dotenv import load_dotenv

load_dotenv()


APP_ID=os.getenv('APP_ID')
API_KEY=os.getenv('API_KEY')

USER_NAME="da71f394d813c70dbdef5466e123c1eb"
PROJECT_NAME="myWorkouts"
SHEET_NAME="workouts"

HOST_DOMAIN= "https://trackapi.nutritionix.com"

nat_lang_endpoint= f"{HOST_DOMAIN}/v2/natural/exercise"

query_params={
    "query": input("ENTER UR EXERCISE")
}

headers={
    "x-app-id":APP_ID,
    "x-app-key": API_KEY
}


data=requests.post(url=nat_lang_endpoint,json=query_params, headers=headers)

print(data.text)


SHEETY_URL="https://api.sheety.co/da71f394d813c70dbdef5466e123c1eb/myWorkouts/workouts"

headers = {
    "Content-Type": "application/json"
}





sheet_params={
    "workout":{

        "date":"08/04/2025",
        "time": "03:00:00",
        "exercise": "Running",
        "duration": "22",
        "calories": "20"
        
    }
}



response= requests.post(url=SHEETY_URL,json=sheet_params,headers=headers)
print(response.text)