# 🌦️ Weather Information App

## 📌 Project Description

The Weather Information App is a Python-based application that allows users to enter a city name and retrieve current weather information using online APIs.

The application uses the Open-Meteo Geocoding API to find the location coordinates and the Open-Meteo Weather API to retrieve current weather data.

## 🎯 Features

* 🌍 Search weather by city name
* 📍 Get latitude and longitude
* 🌡️ Display current temperature
* 💨 Display current wind speed
* ☁️ Display weather condition
* ❌ Handle invalid city names
* 🔒 Handle API connection errors
* 🖥️ Simple command-line interface

## 🛠️ Technologies Used

| Technology     | Purpose                    |
| -------------- | -------------------------- |
| Python         | Application development    |
| Requests       | Sending API requests       |
| Open-Meteo API | Weather and geocoding data |
| JSON           | Processing API responses   |

## 📂 Project Structure

```text
Weather_App/
│
├── weather_app.py
├── weather_app_output.png
└── README.md
```

## ⚙️ How It Works

```text
User enters city
        ↓
Geocoding API
        ↓
Get latitude & longitude
        ↓
Weather API
        ↓
Get current weather data
        ↓
Display weather report
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install Requests

Open the terminal and run:

```bash
python -m pip install requests
```

### 3. Run the application

```bash
python weather_app.py
```

### 4. Enter a city

For example:

```text
Enter city name: Lahore
```

The application will display the current weather information.

## 📸 Output

The program displays:

* City name
* Temperature
* Wind speed
* Weather condition

The output screenshot is included in this project as:

`weather_app_output.png`

## 📚 Concepts Practiced

* Python input/output
* Variables
* Dictionaries
* Conditional statements
* Exception handling
* HTTP requests
* REST APIs
* JSON data
* API response handling
* String formatting

## 🎓 Learning Outcome

Through this project, I learned how to work with external APIs in Python, send HTTP requests using the Requests library, process JSON responses, handle errors, and build a simple real-world command-line application.

## 👨‍💻 Student Project

**Project:** Weather Information App
**Language:** Python
**Type:** Python Developer Internship Task

---

<p align="center">
  🌦️ <b>Weather Information App</b> 🌦️
</p>

<p align="center">
  Built with Python and Open-Meteo API
</p>
