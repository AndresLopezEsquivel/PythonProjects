import datetime
import os
import requests

GENDER = os.environ.get("GENDER")
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APPLICATION_ID")
NUTRITIONIX_APP_KEY = os.environ.get("NUTRITIONIX_APPLICATION_KEY")

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY
}

query = input("What did you do today? \n")

exercise_params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT,
                         json=exercise_params,
                         headers=headers)

exercises_response = response.json()["exercises"]

date = datetime.datetime.now()

exercises_list = [{
    "Date": date.strftime("%d/%m/%Y"),
    "Time": date.strftime("%H:%M:%S"),
    "Exercise": exercise["name"].title(),
    "Duration": exercise["duration_min"],
    "Calories": exercise["nf_calories"]
                    } for exercise in exercises_response]

sheety_headers = {"Authorization": SHEETY_TOKEN}

for exercise in exercises_list:

    workout_sheet_params = {
        "workout": {
            "date": exercise["Date"],
            "time": exercise["Time"],
            "exercise": exercise["Exercise"],
            "duration": exercise["Duration"],
            "calories": exercise["Calories"]
        }
    }

    sheety_response = requests.post(
        url=SHEETY_ENDPOINT,
        json=workout_sheet_params,
        headers=sheety_headers
    )

    print(sheety_response.text)
