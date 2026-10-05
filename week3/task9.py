#For any column create histogram#
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:/FH_DORTMUND/1st_Semester/SEP/PYTHON/WEEK3/dataTitanic.csv")

plt.hist(df["Age"].dropna())

plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.title("Distribution of Passenger Ages")

plt.show()