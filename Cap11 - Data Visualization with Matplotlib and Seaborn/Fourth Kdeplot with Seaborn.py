import seaborn as sea
import random
from matplotlib import pyplot as plt
import pandas as pd


dataSet = pd.DataFrame()
dataSet['Age'] = random.sample(range(20,100),30)
dataSet['Weigth'] = random.sample(range(45,180),30)

sea.kdeplot(dataSet.Weigth)
plt.show()



