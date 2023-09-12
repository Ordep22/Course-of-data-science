import pandas as pd
import numpy as np
from tabulate import tabulate
from pandas import  DataFrame

#Criating a dictionary
data  = {'Satet': ['Santa Catarina', 'Rio de Janeiro', 'Tocatins', 'Bahia',' Minas Gerais'], 'Year':[2004,2005,2006,2007,2008], 'Uneployment Rate':[1,17,16,24,27]}

#From dictionarey create a DataFrame
dataFrame = DataFrame(data)

#Criating a new data frame with the same dicionary
dataFrameOne  = DataFrame(data,columns= ['State','Year','Growth Hate','Unemployment rate'],
                          index= ['StateOne','StateTow','StateThree','StateFour','StateFour'])

#Show the new Data Frame
print(tabulate(dataFrameOne, headers = 'keys', tablefmt = 'psql'))


#Making a Slicing in a DataFrame
#It's most similar to Slicing on a list

#Slicing from a index
print(tabulate(dataFrameOne['StateOne' : 'StateThree'], headers = 'keys', tablefmt = 'psql'))



#Slicing from a range
for i in dataFrameOne['Year']:

    if(i > 2004) & (i< 2008):

        print(i)
    else:
        pass









