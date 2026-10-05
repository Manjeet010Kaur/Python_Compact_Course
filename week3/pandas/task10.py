#Create Correlation Matrix for any column#
import pandas as pd

df = pd.read_csv("E:/FH_DORTMUND/1st_Semester/SEP/PYTHON/WEEK3/dataTitanic.csv")

numeric_data = df[["Age", "Fare", "Pclass", "Survived", "SibSp", "Parch"]]

correlation_matrix = numeric_data.corr()

print("Correlation Matrix:")
print(correlation_matrix)