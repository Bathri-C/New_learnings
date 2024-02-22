import requests
MY_LAT=13.406948
MY_LON=80.110298
# response=requests.get(url="https://cricket.sportmonks.com/api/v2.0/leagues/{ID}")
# response.raise_for_status()
# print(response.status_code)
# # response=requests.get(url="https://cricket.sportmonks.com/api/v2.0/league/{ID}")
# # print(response.status_code)
# data=response.json()

parameters={
    "lat":MY_LAT,
    "lng":MY_LON,
    "formatted":1
}
response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()["results"]
# print(data)
sunrise=data["sunrise"]
sunset=data["sunset"]
print(sunrise)
print(sunset)
#Use split to show only the hour of sunrise and sunset.