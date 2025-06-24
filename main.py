import requests
from datetime import datetime
import os

GENDER = "MALE/FEMALE"
WEIGHT_KG = float("ENTER WEIGHT")
HEIGHT_CM = float("ENTER HEIGHT(cm)")
AGE = int("Enter Age")
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


SHEETY_TOKEN = "Your {•BEARER TOKEN}"
APP_ID = "YOUR APP ID"
API_KEY = "YOUR API KEY"

ex_endpoint = https://trackapi.nutritionix.com/v2/natural/exercise
google_sheet_endpoint = str("Your google sheet endpoint along with the sheet name eg: /workouts") 
print(SHEETY_TOKEN, APP_ID, API_KEY, ex_endpoint, google_sheet_endpoint)

headers_NUT = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

prompt = input("Tell me which exercises you did:").lower()
user_prompt = {
    "query": prompt,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=ex_endpoint, json=user_prompt, headers=headers_NUT)
result = response.json()
print(result)

headers_sheety = {
    "Authorization": SHEETY_TOKEN
}

for exercise in result["exercises"]:
    data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }

    }
    resp = requests.post(url=google_sheet_endpoint, json=data, headers=headers_sheety)

