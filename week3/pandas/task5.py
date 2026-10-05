"""Ex-change 2 columns, use function for it. Sort coulumn by 
name"""
import pandas as pd
df = pd.read_csv("E:/FH_DORTMUND/1st_Semester/SEP/PYTHON/WEEK3/dataTitanic.csv")
def exchange_col(df, col1, col2):
    columns = df.columns.tolist()
    index1 = columns.index(col1)
    index2 = columns.index(col2)
    columns[index1], columns[index2] =  columns[index2], columns[index1] 
    return df[columns]
print("original : ", df.columns.tolist())
df = exchange_col(df, "Age", "Fare")
print("\nAfter exchanging age and fare")
print(df.columns.tolist())
df = df[sorted(df.columns)]
print("\nAfter sorting columns by name ")
print(df.columns.tolist())
