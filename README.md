# Weather App

A simple Python script to fetch current weather data for any city using the OpenWeatherMap API.
This script uses environment variables stored in a `.env` file to keep your API key and other secrets safe.

---

## Features

* Fetch weather data including temperature, humidity, pressure, wind speed, sunrise/sunset, etc.
* Handles errors gracefully when city is not found or API key is invalid.
* Loads sensitive API keys from a `.env` file using `python-dotenv`.
* Clean, readable output.

---

## Prerequisites

* Python 3.6+
* `requests` library
* `python-dotenv` library

---

## Setup

1. **Clone this repository** (or copy the script files).

2. **Install dependencies:**

```bash
pip install requests python-dotenv
```

3. **Create a `.env` file** in the project directory with the following contents:

```
API_KEY=your_openweathermap_api_key
NAME_AUTHOR=Your Name
```

Replace `your_openweathermap_api_key` with your actual API key from [OpenWeatherMap](https://openweathermap.org/api).

---

## Usage

Run the script:

```bash
python weather.py
```

You will be prompted to enter a city name:

```
City Name : London
```

The script will output detailed weather information for the city.

---

## Example Output

```
City: London, Country: GB
Coordinates: 51.51, -0.13
Weather: Clouds - scattered clouds
Temperature: 15°C
Feels Like: 14°C
Min Temp: 13°C
Max Temp: 16°C
Pressure: 1015 hPa
Humidity: 82%
Sea Level: N/A hPa
Ground Level: N/A hPa
Visibility: 10000 meters
Wind Speed: 4.1 m/s
Wind Gust: N/A m/s
Cloudiness: 40%
Sunrise: 2025-07-24 04:58:17
Sunset: 2025-07-24 20:45:30
```

---

## Notes

* Make sure your `.env` file is included in `.gitignore` to avoid exposing your API key in version control.
* The script uses `os.getenv("NAME_AUTHOR")` to read an author name from the environment — feel free to add or remove this as needed.

---

## License

This project is licensed under the MIT License.

---