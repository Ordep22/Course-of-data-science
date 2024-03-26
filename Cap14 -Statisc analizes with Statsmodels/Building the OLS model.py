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













