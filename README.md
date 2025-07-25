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
Rishabh_Kumar
City Name : New Delhi
City: New Delhi, Country: IN
Coordinates: 28.6128, 77.2311
Weather: Clouds - broken clouds
Temperature: 36.75°C
Feels Like: 43.75°C
Min Temp: 36.75°C
Max Temp: 36.75°C
Pressure: 993 hPa
Humidity: 49%
Sea Level: 993 hPa
Ground Level: 967 hPa
Visibility: 10000 meters
Wind Speed: 3.81 m/s
Wind Gust: 4.85 m/s
Cloudiness: 73%
Sunrise: 2025-07-24 05:37:49
Sunset: 2025-07-24 19:17:01
```

---

## Notes

* Make sure your `.env` file is included in `.gitignore` to avoid exposing your API key in version control.
* The script uses `os.getenv("NAME_AUTHOR")` to read an author name from the environment — feel free to add or remove this as needed.

---

## License

This project is licensed under the [MIT License](https://github.com/rishabhkumaar/weather-python/blob/main/LICENSE).

---
