import requests
from credentials import *

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = jt_api_key

weather_params = {
    "lat": 32.613003,
    "lon": -83.624199,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)