import pandas as pd
from pandas import  DataFrame
from tabulate import tabulate

"""
[PT-BR]


[EN]

Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous 
tabular data structure with labeled axes (rows and columns). A Data frame is a 
two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. 
Pandas DataFrame consists of three principal components, the data, rows, and columns.

"""

#Criating a dictionary

data = {'State ': [' Santa Catarina ',  ' Rio de Janeiro', ' Tocantins', ' Bahia', ' Minas Gerais'], 'Year':[2004,2005,2006,2007,2008],
        'Unemployment rate':[1.5,1.7,1.6,2.4,2.7]}

#Convert a dictionary in a Dataframe

dataFrame = DataFrame(data)

#Show the firest lines in the DataFrame

print(f"{dataFrame.head()}")

#Show the type of dataFrame
#print(type(dataFrame))
#<class 'pandas.core.frame.DataFrame'>

#If we can reaorganize the Data Freme, we do this
#print(f"{DataFrame(data,columns= ['State','Year','Unemployment rate'])}")

#Criating a new data frame with the same dicionary
dataFrameOne  = DataFrame(data,columns= ['State','Year','Growth Hate','Unemployment rate'],
                          index= ['StateOne','StateTow','StateThree','StateFour','StateFour'])

#Show the new Data Frame
print(tabulate(dataFrameOne, headers = 'keys', tablefmt = 'psql'))















