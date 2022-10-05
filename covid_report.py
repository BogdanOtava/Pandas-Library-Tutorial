import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("covid_dataframe.csv")

# 1. Show the number of confirmed, deaths and recovered cases in each region.
print(data.groupby("Region").sum())
print(data.groupby("Region")["Confirmed"].sum().sort_values(ascending = False))

print("\n")

# 2. Remove all the records where the confirmed cases are less than 10.
data = data[~(data["Confirmed"] < 10)]
print(data.tail(50))

print("\n")

# 3. Find the region with the highest number of cases recorded.
print(data.groupby("Region")["Confirmed"].sum().sort_values(ascending = False).head(1))

print("\n")

# 4. Find the region with the smallest number of deaths recorded.
print(data.groupby("Region")["Deaths"].sum().sort_values().head(10))

print("\n")

# 5. Find how many confirmed, deaths and recovered cases were recorded in India.
print(data[data["Region"] == "India"])

print("\n")

# 6. Sort the entire dataframe by confirmed cases in ascending order.
print(data.sort_values(by = ["Confirmed"], ascending = True))

print("\n")

# 7. Sort the entire dataframe by recovered cases in descending order.
print(data.sort_values(by = ["Recovered"], ascending = False))