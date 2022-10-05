import pandas as pd

data = pd.read_csv("weather_dataframe.csv")

# 1. Find all the unique 'Wind Speed' values in the dataframe.
print(data["Wind Speed_km/h"].nunique())

print("\n")

# 2. Find exactly when the 'Weather' was 'Clear'.
print(data[data["Weather"] == "Clear"])
print(data.groupby("Weather").get_group("Clear"))

print("\n")

# 3. Find the number of times 'Wind Speed' was exactly 4 km/h.
print(data[data["Wind Speed_km/h"] == 4])

print("\n")

# 4. Find all null values in the dataframe.
print(data.isnull().sum())

print("\n")

# 5. Rename the 'Weather' column to 'Weather Condition'.
print(data.rename(columns = {"Weather": "Weather Condition"}))

print("\n")

# 6. Find the mean 'Visibility'.
print(data["Visibility_km"].mean())

print("\n")

# 7. Find the standard deviation of 'Pressure'.
print(data["Press_kPa"].std())

print("\n")

# 8. Find the variance of 'Relative Humidity'.
print(data["Rel Hum_%"].var())

print("\n")

# 9. Find all instances of 'Snow'.
print(data[data["Weather"].str.contains("Snow")])

print("\n")

# 10. Find all instances where 'Wind Speed' is abouve 24 and 'Visibility' is 25.
print(data[(data["Wind Speed_km/h"] > 24) & (data["Visibility_km"] == 25)])

print("\n")

# 11. Find the mean value of each column against each 'Weather Condition'.
print(data.groupby("Weather").mean())

print("\n")

# 12. What is the minimum and maximum value of each column agains 'Weather Condition'.
print(data.groupby("Weather").min())
print(data.groupby("Weather").max())

print("\n")

# 13. Show all records where 'Weather' is fog.
print(data[data["Weather"].str.contains("Fog")])

print("\n")

# 14. Find all instances where 'Weather' is clear and 'Visibility' is above 40.
print(data[(data["Weather"] == "Clear") | (data["Visibility_km"] > 40)])

print("\n")

# 15. Find all instances where 'Weather' is clear and 'Relative Humidity' is greater than 50, or 'Visibility is above 40.
print(data[(data["Weather"] == "Clear") & (data["Rel Hum_%"] > 50) | (data["Visibility_km"] > 40)])