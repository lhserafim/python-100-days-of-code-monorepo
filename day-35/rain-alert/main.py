import requests
from twilio.rest import Client

# Chave do open weather map
API_KEY = "899ee7723f0d3b8c07a76b39f122eb17"

# Chave do Twillio
account_sid = "AC8aa391212c08e38a761de7f2292ea74c"
auth_token = "3cbf6a2559735504522fc3512ff6f3f9"

MY_LAT = -23.550520  # Your latitude
MY_LONG = -46.633308  # Your longitude

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"  # não traz estes resultados no JSON
}

# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&appid={API_KEY}")
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

# Slice in Python
# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

will_rain = False

# print(weather_data["hourly"][0]["weather"][0])
# Estou usando o slice para poder "fatiar" o Json e só pegar o que me interessa de informação
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    print(hour_data["weather"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella!")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔︎",
            from_="+16197366053",
            to="+5511974880000")
    print(message.status)
