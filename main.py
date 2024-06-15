import requests
from dotenv import load_dotenv
import os
from colorama import init, Fore, Back, Style

# initialize colorama
init(autoreset=True)

# Loads contents of .env file into the script's environment
load_dotenv()

# Give the API key access to the script
API_KEY = os.getenv('API_KEY')

# check to see if this is the same as the API key in the .env file
# print("Your API KEY is: + API_KEY")

# url for api call
url = "https://api.openweathermap.org/data/2.5/weather"


# Ask the user to input the name of a city
city_name = input("Please enter the name of a city: ")
proper_city_name = city_name.capitalize()
# Parameters for the API
request_url = f"{url}?q={city_name}&appid={API_KEY}"

# Make the GET HTTP request
response = requests.get(request_url)

if response.status_code == 200:
    temperature = response.json()['main']['temp']
    temperature_fehrenheit = (round(temperature - 273.15) * 9/5 + 32)
    print(Fore.YELLOW +
          f"The temperature in {proper_city_name} right now is {Fore.GREEN}{temperature_fehrenheit}\u00B0F"
          + Style.RESET_ALL)
    # TODO: Add min temp, max temp, chance of rain, and humidity
    # to the weather report

else:
    print("API call was unsuccessful")
    print(response.json())
