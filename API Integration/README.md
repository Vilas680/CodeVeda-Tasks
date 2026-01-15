API Integration using Python

## 📌 Project Title
API Integration Project (Weather Information App)

## 📝 Description
This project is a Python-based application that connects to an external API to fetch and display real-time data.  
In this project, we use the **OpenWeatherMap API** to get current weather details of any city entered by the user.

The program sends a GET request to the API, processes the JSON response, and displays the data in a user-friendly format.

## 🎯 Objectives
- Learn how to integrate an external API using Python
- Use the `requests` library for HTTP GET requests
- Parse JSON data received from an API
- Handle errors like invalid city names or API failures
- Display real-time weather data in a readable format

## 🛠 Technologies Used
- **Programming Language:** Python  
- **Library:** requests  
- **API:** OpenWeatherMap API  
- **IDE:** VS Code / PyCharm  

API_Integration_Project/
│
├── weather_api.py
├── README.md

## 🔑 API Key Requirement
This project requires an API key from **OpenWeatherMap**.

### Steps to Get API Key:
1. Visit: https://openweathermap.org/api
2. Sign up and log in
3. Go to **My API Keys**
4. Copy your API key
5. Paste it into the code
```python
API_KEY = "YOUR_API_KEY_HERE"

How to Run the Project
Install Python (version 3.x)

Install required library:
pip install requests


Run the program:
python weather_api.py

Enter city name to get weather details

📊 Sample Output
Enter city name: Mumbai

Weather Report:
City: Mumbai
Temperature: 30°C
Humidity: 70%
Weather Condition: Clear Sky
---

## 📂 Project Structure
