#. Transfer object Series into index column of the dataframe#
import pandas as pd
df = pd.read_csv("E:/FH_DORTMUND/1st_Semester/SEP/PYTHON/WEEK3/dataTitanic.csv")
passenger_series = df["PassengerId"]
df.index = passenger_series
print(df.head)
print("\nIndex ", df.index)