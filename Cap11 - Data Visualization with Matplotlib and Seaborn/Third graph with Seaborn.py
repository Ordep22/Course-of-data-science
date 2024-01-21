import random
import seaborn as sea
from matplotlib import  pyplot as plt
import pandas as pd

dataSete = pd.DataFrame()

dataSete['Age'] = random.sample(range(20,100),30)
dataSete['Weigth'] = random.sample(range(20,100),30)

#print(dataSete.head())

#sea.jointplot(data= dataSete, x  = 'Age', y  = 'Weigth', kind='reg')

sea.lmplot(data= dataSete, x  = 'Age', y  = 'Weigth', fit_reg = True)

plt.show()




