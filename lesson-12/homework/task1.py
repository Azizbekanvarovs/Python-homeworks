from bs4 import BeautifulSoup

with open("./lesson-12/homework/weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

rows = soup.select("tbody tr")

forecast = []
for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    forecast.append({"day": day, "temp": temp, "condition": condition})

print("Weather Forecast:")
for entry in forecast:
    print(f"{entry['day']}: {entry['temp']}°C, {entry['condition']}")

max_temp = max(forecast, key=lambda x: x['temp'])["temp"]
sunniest_days = [f['day'] for f in forecast if f['condition'] == "Sunny"]
hottest_days = [f['day'] for f in forecast if f['temp'] == max_temp]

print("\nHottest Day(s):", ", ".join(hottest_days))
print("Sunny Day(s):", ", ".join(sunniest_days))

avg_temp = sum(f['temp'] for f in forecast) / len(forecast)
print(f"Average Temperature: {avg_temp:.2f}°C")
