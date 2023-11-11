import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
data = load_iris()
dataFrame = pd.DataFrame(data['data'],columns= data['feature_names'])
dataFrame['species'] = data['target']

print("Iris dataFrame is:")
print(dataFrame.head())

#In this point we going to show a simple graph with our dataFrame
'''
NONTE: if you aren't following along in a Jupter Notbool or in a IPython
shell, the you'll need to use the pyplot interface from matplotlib to display
the plot.
'''
dataFrame.plot()
plt.show()

#In this next graph we going to show a scater plot. It's responseble to show
#disperciosn between some varibles

dataFrame.plot.scatter(x = 'sepal length (cm)', y = 'sepal width (cm)')
plt.show()

#In this next graph we going to show a area graphic.
columns = ['sepal length (cm)', 'petal length (cm)','petal width (cm)', 'sepal width (cm)']
dataFrame[columns].plot.area()
plt.show()










