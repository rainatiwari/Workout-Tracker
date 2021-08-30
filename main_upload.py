import requests
from datetime import datetime

APP_ID = YOUR_APP_ID
API_KEY = YOUR_API_KEY

GENDER = YOUR_GENDER (male/female)
WEIGHT_KG = YOUR_WEIGHT
HEIGHT_CM = YOUR_HEIGHT
AGE = YOUR_AGE

url_endpoint = "https://trackapi.nutritionix.com/v2"
sheet_endpoint = YOUR_SHEET_ENDPOINT

#Bearer Token Authentication
bearer_headers = {
    "Authorization": "Bearer YOUR_BEARER_TOKEN"
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_text = input("Tell me which exercises you did: ")
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_endpoint = f"{url_endpoint}/natural/exercise"

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# ################## Start of Step 4 Solution ######################
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
# print(today_date)
# print(now_time)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

print(sheet_response.text)

