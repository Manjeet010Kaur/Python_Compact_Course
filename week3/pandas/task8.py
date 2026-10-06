import pandas as pd

dict1 = {
    "ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
}

dict2 = {
    "ID": [1, 2, 3],
    "Age": [20, 25, 30]
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

merged = pd.merge(df1, df2, on="ID")

print("Merged:")
print(merged)

result = pd.concat([df1, df2], axis=1)

print("\nAppended as columns:")
print(result)