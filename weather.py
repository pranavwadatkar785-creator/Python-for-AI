import requests

# We need coordinates to get weather data
latitude = 18.6801   # Moshi latitude
longitude = 73.8502   # Moshi longitude

def getweather(latitude,longitude):
    # Build the API URL with our parameters
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    # Make the request
    response = requests.get(url)
    data = response.json()

    return data["current"]["temperature_2m"]

print(f"Temperature in moshi is {getweather(latitude,longitude)}")