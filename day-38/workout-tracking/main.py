import requests
from datetime import datetime
import os

# Set environment variables
os.environ["APP_ID"] = "cab4955e"
os.environ["API_KEY"] = "2c49ab6e748e3c894aa66a8328219fe9"
os.environ["TOKEN"] = "e3c894aa66a832"

# Get environment variables
print(os.environ.get("APP_ID"))
print(os.environ.get("API_KEY"))
print(os.environ.get('TOKEN'))

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("API_KEY")

SHEET_ENDPOINT = "https://api.sheety.co/e46d707e5a0b52dbb7f100e68d3235fe/myWorkoutsPython/workouts"

# Basic Authentication
# sheet_response = requests.post(
#   sheet_endpoint,
#   json=sheet_inputs,
#   auth=(
#       YOUR USERNAME,
#       YOUR PASSWORD,
#   )
# )

# Bearer Token Authentication
SHEET_HEADERS = {"Authorization": f"Bearer {os.environ.get('TOKEN')}"}


GENDER = "male"
WEIGHT_KG = 92
HEIGHT_CM = 180.00
AGE = 38

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": 30
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=parameters, headers=header)
print(response.json())
result = response.json()

# Start of Step 4 Solution

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Pego o meu retorno da API (result), e percorro ele como uma lista. Monto o meu dicionário dentro de outro dicionário
# combinando os dados retornados em result com as colunas do meu excel
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

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=SHEET_HEADERS)

    print(sheet_response.text)
