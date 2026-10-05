""" Change the data in the column of DataFrame according to 
some condition """
import pandas as pd
df = pd.read_csv("E:/FH_DORTMUND/1st_Semester/SEP/PYTHON/WEEK3/dataTitanic.csv")
print("before changing : ")
print(df[["PassengerId", "Fare"]].head(20))
df.loc[df["Fare"]>50, "Fare"] = 50
print("\nAfter changing: ")
print(df[["PassengerId", "Fare"]].head(50))