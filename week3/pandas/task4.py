"""Get names of the DataFrame columns and sum of losted 
values DF """
import pandas as pd
df = pd.read_csv("E:/FH_DORTMUND/1st_Semester/SEP/PYTHON/WEEK3/dataTitanic.csv")
print(df.columns)
print(df.isnull().sum())
