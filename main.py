import pandas as pd

data = pd.read_csv("heart.csv")
print(data.head())
print(data.isnull().sum())
