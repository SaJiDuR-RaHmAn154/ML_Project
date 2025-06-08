import pandas as pd
import pickle

data = pd.read_csv("Heart_Disease_Prediction.csv")
print(data.head())
print(data.isnull().sum())
features = data[["Age", "Chest pain type", "BP", "Cholesterol", "Max HR", "ST depression", "Number of vessels fluro", "Thallium"]]
target = data['Heart Disease']

print(features)
print(target)
