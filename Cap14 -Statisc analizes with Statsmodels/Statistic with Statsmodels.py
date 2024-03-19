import pandas as pd
import numpy as np
import seaborn as sea
import  matplotlib.pyplot as plt
import  statsmodels.api as sn

data = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap14 -Statisc analizes with Statsmodels/Data/dataset.csv")
dataFrame   = pd.DataFrame(data)
print(dataFrame.head())
print("\n")
print(f"Shape: {dataFrame.shape}")
print("\n")
print(f"Number of columns: {dataFrame.columns}")
print("\n")
print(f"Info: {dataFrame.info()}")

#Starting the exploration analyse

#Check if there are any null values
print(30*"--")
print("Count of null values")
print(dataFrame.isnull().sum())

#Statistic resume
print(30*"--")
print("Statistic resume")
print(dataFrame.describe())






