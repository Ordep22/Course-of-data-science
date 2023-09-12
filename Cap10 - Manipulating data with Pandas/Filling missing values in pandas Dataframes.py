import pandas as pd
import numpy as np
from tabulate import tabulate

"""
[PT-BR]

A função fillna() é usada para preencher os valores ausentes. A função oferece muitas opções.
Podemos usear um valore específico, uma função agregada (por exemplo, média) ou o valor anterior ou seguinte.
Para esse exemplo usaremos a moda, a estatística que representa o vaçp que aparece mais vezes em uma variável.
A moda em estetistica é uma medida de tedência central que representa o valor mais freuqnete em um conjutno de dados. 
A moda é especialemnte útil quando queremos saber qual é o valor mais comum ou popular em um conjunto de dados, seja em um distribuição unimodal
(com apenas uma moda) ou em uma distribuição bimodal (com duas modas).
No entanto, a moda pode não ser taço representativa quanto outras medidas de tendência central, 
como a média e a mediana, especialmente em distribuições assimétricas ou quando há valore extremos. 
Por essa razão, é importante analizar diferentes medidas de tedência central e usar a que melhor se adequa aos objetivos da análise estatistica.


[EN]

The fillna() function is used to fill in missing values. The function offers many options. 
We can use a specific value, an aggregate function (e.g., mean), or the previous or next value. 
For this example, we will use the mode, which is the statistic representing the value that appears most frequently in a variable.
Mode in statistics is a measure of central tendency that represents the most frequently occurring value in a dataset. 
Mode is especially useful when we want to know what the most common or popular value is in a dataset, 
whether in a unimodal distribution (with only one mode) or in a bimodal distribution (with two modes).
However, the mode may not be as representative as other measures of central tendency, such as the mean and median, 
especially in asymmetric distributions or when there are extreme values. For this reason, it is important to 
analyze different measures of central tendency and use the one that best suits the goals of statistical analysis.


"""

#Read a data frame
dataFrame = pd.read_csv("chord-progressions.csv")


##Show the head of data frame

print(f"{tabulate(dataFrame.head())}")

#Find a NaN value

numbersOfNan = dataFrame.isna().sum()
print(f"There are {numbersOfNan} in the dataset!")

#Extract moda of colunm Progression Quality
moda  = dataFrame["4th chord"].value_counts().index[0]
print(f"The most comum value in the 4th chord is: {moda}")

#Insert the molst commun values on the dataFrame
dataFrame["4th chord"].fillna(value = moda, inplace = True) #inplace = True means that the value is going to insert on a dataframe, not a copy his

#Show the new dataFrame
print(f"The new data frame is \n{dataFrame.head(15)}")

