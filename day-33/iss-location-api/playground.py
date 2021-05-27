# https://httpstatuses.com/
import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()  # Lança uma exceção do tipo HTTP em caso de erro
# print(response)
# print(response.json())
# print(response.json()["iss_position"]["longitude"])  # pegando a informação do JSON
#
# # criando uma tupla
# iss_position = (response.json()["iss_position"]["latitude"], response.json()["iss_position"]["longitude"])
# print(iss_position)

# https://sunrise-sunset.org/api
parameters = {
    "lat": -23.550520,
    "lng": -46.633308,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(response.json())
print(response.json()["results"]["sunrise"])
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]  # Quero pegar a hora apenas
print(sunrise)

time_now = datetime.now()
print(time_now)










