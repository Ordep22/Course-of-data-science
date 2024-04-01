import pandas as pd
import os
from matplotlib import pyplot as plt
import numpy as np
import  statsmodels.api as sn

path = os.getcwd() + "/Data/dataset.csv"

data  = pd.read_csv(path)

dataSet  = pd.DataFrame(data)

#print(dataSet.head())

#Define the  dependent variable

dependentVariable = dataSet['valor_aluguel']

#Defining the independent variable

independentVariable = dataSet['area_m2']

#The statsmodel needs the addition of an constant to independent variable

independentVariable = sn.add_constant(independentVariable)

model = sn.OLS(dependentVariable,independentVariable)

result = model.fit()

print("\n")
print(result.summary())

#Showing the result by a linear regression graph
plt.figure(figsize =  (12,8))
plt.xlabel("area_m2",size  = 16)
plt.ylabel('valor_aluguel',size  = 16)
plt.plot(independentVariable["area_m2"],dependentVariable, "o", label = "Dados Reais")
plt.plot(independentVariable["area_m2"],result.fittedvalues, "r-", label  = "Regression Line (Prevision Model)")
plt.legend(loc = "best")
plt.savefig(os.getcwd() + "/Linear_Regression.png")














