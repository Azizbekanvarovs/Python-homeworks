import requests

city = "Tashkent"
api_key = "90bdd4f3d47a4eff1b7b987451a61c97"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather = data['weather'][0]['description']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather}")
else:
    print("Failed to retrieve data:", response.status_code)
