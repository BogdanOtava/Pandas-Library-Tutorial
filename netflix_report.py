import pandas as pd

data = pd.read_csv("netflix_dataframe.csv")

"""
print(data.head())      # -> shows the first N rows in the dataframe. Default is 5.
print(data.tail())      # -> shows the last N rows in the dataframe. Default is 5.
print(data.shape)       # -> shows the total number of rows and columns of the dataframe.
print(data.size)        # -> shows the total number of elements in the dataframe.
print(data.columns)     # -> shows each column name.
print(data.dtypes)      # -> shows the data-type of each column.
print(data.info())      # -> shows indexes, columns, data-types of each column, memory at once.
"""

# 1. Find the duplicate record in the dataframe. Remove the duplicates.
print(data[data.duplicated()]) # -> checking if there are any duplicate elements in the dataframe.

data.drop_duplicates(inplace = True) # -> removing any duplicate elements in the dataframe.

print("\n")

# 2. Find null values in each column.
print(data.isnull().sum()) # -> shows null values.

print("\n")

# 3. Find the show ID and the Director of "House of Cards".
print(data[data["Title"].isin(["House of Cards"])])
print(data[data["Title"].str.contains("House of Cards")])

print("\n")

# 4. Find the year with the most movie and show releases.
print(data.dtypes)
data["Date_N"] = pd.to_datetime(data["Release_Date"]) # -> creating a new datetime column.
print(data.head())
print(data.dtypes)

print(data["Date_N"].dt.year.value_counts()) # -> counts the ocurrence of all individual years.

print("\n")

# 5. Find how many movies and shows are in the dataframe.
print(data.groupby("Category").Category.count())

print("\n")

# 6. Show all the movies that were released in 2015.
data["Year"] = data["Date_N"].dt.year # -> creating a new year column from the datetime column.

print(data[(data["Category"] == "Movie") & (data["Year"] == 2015)]) # -> filters the dataframe by movie and by year so it will return all the movies released in 2015.

print("\n")

# 7. Show all titles and movies released in the Brazil.
print(data[(data["Category"] == "TV Show") & (data["Country"] == "Brazil")])

print("\n")

# 8. Show Top 10 Directors, who gave the highest number of TV Shows and Movies to Netflix.
print(data["Director"].value_counts().head(10))

print("\n")

# 9. Show all records where the category is 'Movie' and the type is 'Comedy', or country is 'United Kingdom'.
print(data[(data["Category"] == "Movie") & (data["Type"] == "Comedies") | (data["Country"] == "United Kingdom")])

print("\n")

# 10. Find all the Movies and TV Shows that casted Tom Cruise.
print(data[data["Cast"] == "Tom Cruise"]) # -> this won't work because Tom Cruise isn't the only element in the Cast row.

data_new = data.dropna()
print(data_new[data_new["Cast"].str.contains("Tom Cruise")])

print("\n")

# 11. Find what are the different ratings defined by Netflix.
print(data["Rating"].nunique()) # -> returns an integer with the number of unique elements.
print(data["Rating"].unique()) # -> returns a list with all the unique elements.

print("\n")

# 12. Find how many Movies got the 'TV-14' rating in Canada.
print(data[(data["Category"] == "Movie") & (data["Rating"] == "TV-14") & (data["Country"] == "Canada")].shape)

print("\n")

# 13. Find how many TV Shows got the 'R' rating after 2018.
print(data[(data["Category"] == "TV Show") & (data["Rating"] == "R") & (data["Year"] > 2018)])

print("\n")

# 14. Find the maximum duration of a Movie/TV Show on Netflix.
print(data["Duration"].unique())
data[["Minutes", "Unit"]] = data["Duration"].str.split(" ", expand = True) # -> creating from the Duration column two different columns - Minutes and Units.

print(data["Minutes"].max())

print("\n")

# 15. Find which country has the highest number of TV Shows.
tvshow_data = data[data["Category"] == "TV Show"]
print(tvshow_data["Country"].value_counts().head(1))

print("\n")

# 16. Sort the dataframe by Years.
print(data.sort_values("Year").head(10))
print(data.sort_values("Year", ascending = False).head(10))

print("\n")

# 17. Find the instances where category is 'Movie' and type is 'Drama', or category is 'TV Show' and type is 'Kids' TV'
print(data[(data["Category"] == "Movie") & data["Type"].str.contains("Dramas") | (data["Category"] == "TV Show") & (data["Type"].str.contains("Kids' TV"))])
