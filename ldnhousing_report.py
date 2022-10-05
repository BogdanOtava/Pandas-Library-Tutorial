import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("ldnhousing_dataframe.csv")

# 1. Convert the 'date' column to Datetime format.
data["date"] = pd.to_datetime(data["date"])
print(data.head(50))
print(data.dtypes)

print("\n")

# 2. Add a new column which contains only the year.
data["year"] = data["date"].dt.year
print(data.head())

print("\n")

# 3. Add a new column 'month' as the 2nd column.
data.insert(2, "month", data["date"].dt.month)
print(data.head())

print("\n")

# 4. Remove the columns 'year' and 'month' from the dataframe.
data.drop(["month", "year"], axis = 1, inplace = True)
print(data.head())

print("\n")

# 5. Find how many records of 0 crimes are in the dataframe.
print(len(data[data["no_of_crimes"] == 0]))

print("\n")

# 6. Find the maximum and minimum 'average_price' per year.
data["year"] = data["date"].dt.year
print(data.groupby("year")["average_price"].max())
print(data.groupby("year")["average_price"].min())

# 7. Find the mean 'no_of_crimes' per area.
print(data.groupby("area")["no_of_crimes"].mean().sort_values(ascending = True))