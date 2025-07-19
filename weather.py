import requests
from ss import *
key2='40f8ff8bf1e473beedeab4c01c04865c'
api_address = 'https://api.openweathermap.org/data/2.5/weather?lat=25.3176&lon=82.9739&appid='+key2

json_data=requests.get(api_address).json()

def temp():
    temperature=round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description=json_data["weather"][0]["description"]
    return description

#print(temp())
#print(des())