import requests
from credentials import *

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = jt_api_key

weather_params = {
    "lat": 32.613003,
    "lon": -83.624199,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
       will_rain = True  

if will_rain:
    print("Bring an umbrella!")