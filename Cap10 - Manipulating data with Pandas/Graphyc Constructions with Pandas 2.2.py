import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

data = load_iris()
dataFrame = pd.DataFrame(data['data'],columns = data['feature_names'])
dataFrame['species'] = data['target']

print("Iris dataFrame is:")
print(dataFrame.head())


#Now we goig to crate a bar graph from datas
dataFrame.groupby('species').mean().plot.bar()
plt.show()

#Now we going to crate a pie graph
dataFrame.groupby('species').count().plot.pie(y = 'sepal length (cm)')
plt.show()

#Now we going to crate a KDE graphic,
dataFrame.plot.kde(subplots = True, figsize = (8,8))
plt.show()

columns = ['sepal length (cm)', 'petal length (cm)','petal width (cm)', 'sepal width (cm)']
dataFrame[columns].plot.box(figsize = (8,8))
plt.show()




