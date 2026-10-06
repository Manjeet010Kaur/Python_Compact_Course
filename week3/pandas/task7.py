import pandas as pd

df = pd.read_csv("E:/FH_DORTMUND/1st_Semester/SEP/PYTHON/WEEK3/dataTitanic.csv")

avg_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(avg_age)

print(df["Age"].isnull().sum())
print(df["Age"].head(20))