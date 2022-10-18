import pandas as pd

data = pd.read_csv("police_dataframe.csv")

# 1. Data cleaning. Remove the column that contains only missing values.
data.drop(columns = "country_name", inplace = True)
print(data.head(50))

print("\n")

# 2. Filtering and value counts. Find who got stopped more oftern for speeding.
print(data[data["violation"] == "Speeding"].driver_gender.value_counts())

print("\n")

# 3. Find if gender affects who gets searched during a stop.
print(data.groupby("driver_gender").search_conducted.sum())

print("\n")

# 4. Find the mean for stop_duration.
data["stop_duration"] = data["stop_duration"].map({"0-15 Min": 7.5, "16-30 Min": 24, "30+ Min": 45})
print(data["stop_duration"].mean())

print("\n")

# 5. Compare the age distribution for each violation.
print(data.groupby("violation").driver_age_raw.describe())
