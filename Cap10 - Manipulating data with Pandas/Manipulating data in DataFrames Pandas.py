from datetime import date

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

 - NaN: Not Any number
 
"""

#Criating a dictionary

data = {'State ': ['Santa Catarina','Rio de Janeiro','Tocantins','Bahia','Minas Gerais'], 'Year':[2004,2005,2006,2007,2008],
        'Unemployment rate':[1,1.7,1.6,2.4,2.7]}

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


#Show values in the Data frame
print(f"The value in the tada frame are:\n{dataFrameOne.values}")

#Show Dtypes
print(f"The types in the tada frame are:\n{dataFrameOne.dtypes}")

#Show the lines of the colunm
#Share if it´s possible to show part of the data frame in a tabulate model
#print(f"The types in the tada frame are:\n{tabulate(dataFrameOne['State'], headers = 'keys', tablefmt = 'psql')}")

print(f"The the lines of the colunm are:\n{dataFrameOne['State']}")


#Finda an index (it´s the line index)
print(f"The the lines of the colunm are:\n{dataFrameOne.index}")

#Show the specific colunm with .filter
print(f"The specifc line in the data frame are:\n{dataFrameOne.filter(items=['State'], axis=1)}")

#Show the specific line with .filter Isso est
print(f"The specifc line in the data frame are:\n{dataFrameOne.filter(items=['StateOne'], axis=1)}")

























