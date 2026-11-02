
import json
import pandas as pd

# Sample JSON weather data
weather_json = '''
{
    "cities": [
        {
            "location": {"city": "Thrissur", "country": "India"},
            "weather": {"temperature": 30, "humidity": 75}
        },
        {
            "location": {"city": "Kochi", "country": "India"},
            "weather": {"temperature": 32, "humidity": 80}
        },
        {
            "location": {"city": "Kozhikode", "country": "India"},
            "weather": {"temperature": 29, "humidity": 70}
        }
    ]
}
'''

# Parse JSON data
data = json.loads(weather_json)

# Convert nested JSON into a table
df = pd.json_normalize(data["cities"])

# Select required columns
df = df[[
    "location.city",
    "location.country",
    "weather.temperature",
    "weather.humidity"
]]

# Rename columns
df.columns = ["City", "Country", "Temperature", "Humidity"]

# Display weather details
print("WEATHER REPORT")
print(df.to_string(index=False))

# Display summary for each city
print("\nCITY-WISE WEATHER SUMMARY")

for _, row in df.iterrows():
    print(
        f"{row['City']}: "
        f"Temperature = {row['Temperature']}°C, "
        f"Humidity = {row['Humidity']}%"
    )

# Overall summary
print("\nOVERALL SUMMARY")
print("Average Temperature:", df["Temperature"].mean(), "°C")
print("Average Humidity:", df["Humidity"].mean(), "%")
print("Hottest City:", df.loc[df["Temperature"].idxmax(), "City"])
