import pandas as pd
import numpy as np
import seaborn as sea
import random
from matplotlib import  pyplot as plt

np.random.seed(42)
n = 1000
percentSmokers  = 0.2

#Variables
flagSmokers  = np.random.rand(n) < percentSmokers
age  = np.random.normal(40,10,n)
height = np.random.normal(170,10,n)
weight  = np.random.normal(70,10,n)

data  = pd.DataFrame({'Height': height, 'Weight':weight,'Smokers':flagSmokers})
data['Smokers'] = data['Smokers'].map({True:'Smoker', False: 'No Smoker'})
#print(data.head())

# Style

sea.set(style = "ticks")

sea.lmplot(x = "Height", y ="Weight", data = data,  hue= 'Smokers',palette= ['tab:blue','tab:orange'], height=7 )

plt.xlabel("Height (cm)")
plt.ylabel("Weight (Kg)")
plt.title("Relation bettween Weight and Height of smokers and nonsmokers")
sea.despine()
plt.show()




