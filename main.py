import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "acf56932bb2b2a76d6da7713614a1d32"

#MY_LAT = 51.507351 # Your latitude
#MY_LONG = -0.127758 # Your longitude

MY_LAT = 22.500620 # Your latitude
MY_LONG = 88.360340 # Your longitude

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    #can exclude parameters
    #"exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params )
#Check if we get 200 reponse code to confirm that api call is created correctly
#print(response.status_code)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

zero_hour_weather = weather_data["hourly"][0]
print(zero_hour_weather)

#Accessing the weather id code of the 0th hour
#weather_data["hourly"][0]["weather"][0]["id"]

##Determining whether or not we need to bring an umbrella based on just id codes of the first 12 hours

#Accessing all of the weather data from the first 12 hours
weather_slice = weather_data["hourly"][:12]

will_rain = False

#Need to loop through in order to collect just the id codes from each hour
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
else:
    print("Don't need an umbrella-no precipitation today!!")