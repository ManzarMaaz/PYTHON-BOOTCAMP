import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# ------------------- Load environment variables -------------------
load_dotenv()

APP_ID = os.getenv("NIX_APP_ID")
API_KEY = os.getenv("NIX_API_KEY")
NL_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

GENDER = os.getenv("GENDER")
WEIGHT_KG = float(os.getenv("WEIGHT_KG"))
HEIGHT_CM = float(os.getenv("HEIGHT_CM"))
AGE = int(os.getenv("AGE"))

# ------------------- User Input -------------------
exercise_text = input("Tell me which exercise(s) you did: ")

# ------------------- Call Nutritionix -------------------
headers_nutritionix = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(NL_EXERCISE_ENDPOINT, json=parameters, headers=headers_nutritionix)
result = response.json()

if "exercises" not in result:
    print("Error fetching exercise data:", result)
    exit()

# ------------------- Current Date & Time -------------------
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

# ------------------- Send to Sheety -------------------
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": int(exercise["duration_min"]),
            "calories": int(exercise["nf_calories"])
        }
    }

    sheety_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
    )

    if sheety_response.status_code in [200, 201]:
        print(f"Logged {exercise['name'].title()} successfully!")
        print(sheety_response.text,'\n\n')
    else:
        print("Failed to log exercise:", sheety_response.status_code, sheety_response.text)
