import seaborn as sea
import random
import pandas as pd
from matplotlib import pyplot as plt

dataSet  = pd.DataFrame()

dataSet['Age'] = random.sample(range(20,100),30)
dataSet['Weigth'] = random.sample(range(45,180),30)


sea.violinplot(dataSet.Age)
plt.show()





