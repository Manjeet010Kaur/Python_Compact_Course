""" Replay ( Apply) missed values in the Column with average 
values. """
import pandas as pd
df = pd.read_csv("E:/FH_DORTMUND/1st_Semester/SEP/PYTHON/WEEK3/dataTitanic.csv")
print("age values before")
print(df["Age"].isnull().sum())
avg_age = df["Age"].mean()
print("\naverage age", avg_age)
df["Age"] = df["Age"].fillna(avg_age)
print("\nMissing Age values after:")
print(df["Age"].isnull().sum())
print("\nAge column:")
print(df["Age"].head(20))