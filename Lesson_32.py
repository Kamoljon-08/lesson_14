import requests
clear__list = []

url = "https://api.openweathermap.org/data/2.5/onecall?lat=39.634087&lon=-8.819204&exclude=current&appid=de3ae2261305416619b29ff9f5edc781&units=metric"
req__body = requests.get(url)
req__json = req__body.json()

def CLEAR(i):
    clear__list.append({
    "day__data": i["temp"]["day"],
    "min__data": i["temp"]["min"],
    "max__data": i["temp"]["max"],
    "night__data": i["temp"]["night"], 
    "eve__data": i["temp"]["eve"], 
    "morn__data": i["temp"]["morn"],  
    })

for i in req__json["daily"]:
    CLEAR(i)

for i in clear__list:
    print(i)