import requests
from scipy.constants import convert_temperature
import os


api_key = "8d84bc6b5317cd86ebd5757238144054"


while True:
    user_input = input("Enter a City name (or 'quit' to exit): ").lower()
    if user_input == "quit":
        break

    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")

    if response.status_code == 200:

        os.system('cls' if os.name == 'nt' else 'clear')  
        
        data = response.json()
        temp = data['main']['temp']
        precipitation = data['weather'][0]['description']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print()
        print(f"Weather Information for {user_input.capitalize()}:")
        print("-------------------------------")

        print(f"Temperature (°F): {round(convert_temperature(temp, 'K', 'F'), 2)}°F")
        print(f"Temperature (°C): {round(convert_temperature(temp, 'K', 'C'), 2)}°C")
        print(f"Weather: {precipitation}")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

        print("-------------------------------")
    else:
        print(f"City '{user_input}' not found. Please try again.")  
