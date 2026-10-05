"""8.Create two data frames using the two Dicts, Merge two 
data frames, and append the second data frame as a new 
column to the first data frame. """
import pandas as pd


dict1 = {
    "ID": [1, 2, 3],
    "Name": ["Manjeet", "Asha", "John"]
}

dict2 = {
    "ID": [1, 2, 3],
    "City": ["Dortmund", "Delhi", "Berlin"]
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

merged = pd.merge(df1, df2, on="ID")

print("\nMerged DataFrame:")
print(merged)


result = pd.concat([df1, df2], axis=1)

print("\nDataFrame after appending columns:")
print(result)