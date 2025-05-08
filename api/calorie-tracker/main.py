import requests
import os
from dotenv import load_dotenv

import datetime as dt

load_dotenv()


APP_ID=os.getenv('APP_ID')
API_KEY=os.getenv('API_KEY')

AUTH_HEADER=os.getenv('AUTH_HEADER')

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

data=data.json()

res=[]


for i in range(len(data["exercises"])):
    res.append([data["exercises"][i]['name'],data["exercises"][i]['duration_min'],data["exercises"][i]['nf_calories']])

print(res)


SHEETY_URL="https://api.sheety.co/da71f394d813c70dbdef5466e123c1eb/myWorkouts/workouts"

headers = {
    "Content-Type": "application/json",
    "Authorization": AUTH_HEADER
}



date=dt.datetime.now().strftime("%d/%m/%Y")
time=dt.datetime.now().strftime("%H:%M:%S")


for i in range(len(res)):
    sheet_params={
        "workout":{

            "date": date,
            "time": time,
            "exercise": res[i][0],
            "duration": str(res[i][1]),
            "calories": str(res[i][2])
            
        }
    }



    response= requests.post(url=SHEETY_URL,json=sheet_params,headers=headers)
    print(response.text)