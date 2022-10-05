import pandas as pd

data = pd.read_csv("cars_dataframe.csv")

# 1. Data Cleaning. Find all the null values in the dataframe. If there are any null values in any column, then fill it with the mean of that column.
print(data.isnull().sum())
data["Cylinders"].fillna(data["Cylinders"].mean(), inplace = True)

print(data.isnull().sum())

print("\n")

# 2. Find the different types of 'Make' in the dataframe and the count of each 'Make'.
print(data["Make"].value_counts())

print("\n")

# 3. Filtering. Shouw all records where 'Origin' is Asia or Europe.
print(data[(data["Origin"] == "Asia") | (data["Origin"] == "Europe")])

print(data[data["Origin"].isin(["Asia", "Europe"])])

print("\n")

# 4. Removing unwanted records. Remove all records where 'Weight' is above 4000.
print(data[~(data["Weight"] > 4000)])

print("\n")

# 5. Apply function on a column. Increase all values of 'MPG_City' by 3.
data["MPG_City"] = data["MPG_City"].apply(lambda x:x + 3)
print(data.head())