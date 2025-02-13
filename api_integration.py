import requests

def get_weather(city_name, api_key):
    # Define the endpoint and parameters
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    
    # Send the GET request to the OpenWeather API
    response = requests.get(url)
    
    # Check if the response status is OK
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract relevant weather data
        main_weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        
        # Display the weather information
        print(f"Weather in {city_name}: {main_weather} ({description})")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        # Handle errors (e.g., city not found)
        print(f"Error: {response.status_code}. Unable to fetch data for {city_name}")

# Input from the user for city name
city = input("Enter the city name: ")

# Your OpenWeather API key
api_key = "af41b5bd6231fd2c1b22a84523819f0a"

# Get the weather data for the specified city
get_weather(city, api_key)
