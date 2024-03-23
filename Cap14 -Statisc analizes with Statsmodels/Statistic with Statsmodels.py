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

#Rusume of target varible
print(30*"--")
print("Resume of target variable")
print(dataFrame['valor_aluguel'].describe())

#Show the informations in a graph
sea.histplot(data = dataFrame, x = 'valor_aluguel',kde= True)
plt.savefig("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap14 -Statisc analizes with Statsmodels/Hist_valor_aluguel.png")
plt.close()

#Correlation matrix
print(30*"--")
print("Correlation Matrix")
print(dataFrame.corr())

sea.scatterplot(data = dataFrame, x = "area_m2", y = "valor_aluguel")
plt.savefig("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap14 -Statisc analizes with Statsmodels/Correlation_Graph.png")
plt.close()










