import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the API key from the environment
API = os.getenv("API_KEY")
print(os.getenv("NAME_AUTHOR"))
def format_time(unix_time):
    return datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')

text = input("City Name : ")
cityname = "+".join(text.strip().split())

url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&units=metric&appid={API}"
response = requests.get(url)
data = response.json()

if response.status_code != 200:
    print("Error fetching data:", data.get("message", "Unknown error"))
else:
    print(f"City: {data['name']}, Country: {data['sys']['country']}")
    print(f"Coordinates: {data['coord']['lat']}, {data['coord']['lon']}")
    print(f"Weather: {data['weather'][0]['main']} - {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels Like: {data['main']['feels_like']}°C")
    print(f"Min Temp: {data['main']['temp_min']}°C")
    print(f"Max Temp: {data['main']['temp_max']}°C")
    print(f"Pressure: {data['main']['pressure']} hPa")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Sea Level: {data['main'].get('sea_level', 'N/A')} hPa")
    print(f"Ground Level: {data['main'].get('grnd_level', 'N/A')} hPa")
    print(f"Visibility: {data['visibility']} meters")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
    print(f"Wind Gust: {data['wind'].get('gust', 'N/A')} m/s")
    print(f"Cloudiness: {data['clouds']['all']}%")
    print(f"Sunrise: {format_time(data['sys']['sunrise'])}")
    print(f"Sunset: {format_time(data['sys']['sunset'])}")
