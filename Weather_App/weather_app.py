import requests

print("================================")
print("       WEATHER INFORMATION")
print("================================")

city = input("Enter city name: ")

url = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
except requests.exceptions.RequestException:
    print("Error: Unable to connect to the weather service.")
    exit()



data = response.json()

if "results" in data and len(data["results"]) > 0:
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    print("Latitude:", latitude)

    print("Longitude:", longitude)

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,weather_code"
    }

    try:
        weather_response = requests.get(weather_url, params=weather_params)
        weather_response.raise_for_status()
    except requests.exceptions.RequestException:
        print("Error: Unable to get weather information.")
        exit()

    

    weather_data = weather_response.json()

    temperature = weather_data["current"]["temperature_2m"]
    wind_speed = weather_data["current"]["wind_speed_10m"]


    weather_code = weather_data["current"]["weather_code"]

    if weather_code == 0:
        condition = "Clear Sky"
    elif weather_code in [1, 2, 3]:
        condition = "Cloudy"
    elif weather_code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
        condition = "Rainy"
    elif weather_code in [71, 73, 75, 77, 85, 86]:
        condition = "Snowy"
    else:
        condition = "Other"
        
    print()
    print("================================")
    print("        WEATHER REPORT")
    print("================================")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Wind Speed:", wind_speed, "km/h")
    print("Condition:", condition)
    print("================================")
else:
    print("City not found!")