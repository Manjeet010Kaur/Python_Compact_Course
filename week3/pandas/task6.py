#Delete upper and lower 5% in object DataFrame #
import pandas as pd
df = pd.read_csv("E:/FH_DORTMUND/1st_Semester/SEP/PYTHON/WEEK3/dataTitanic.csv")
print("original numbers of row: ", len(df))
lower = df["Fare"].quantile(0.05)
upper = df["Fare"].quantile(0.95)
print("lower 5% limit", lower)
print("upper 5% limit", upper)
df = df[(df["Fare"] >= lower) & (df["Fare"] <= upper)]
print("number of rows after removing lower and upper 5% ", len(df))
print("\nfirts 10 rows")
print(df[["PassengerId", "Fare"]].head(10))