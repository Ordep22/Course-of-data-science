import matplotlib.pyplot as plt
import pandas as pd

from libraries import *

data  = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/dados/dataset.csv")

dataFrame   = pd.DataFrame(data)

print('\n')
print(15*"--" + ' Q2 ' + 15*"--")
print("Calculate the total of sales per date")
print(30*"--")

#sales_per_date = dataFrame['Data_Pedido'].value_counts()
sales_per_date = dataFrame.groupby('Data_Pedido')['Valor_Venda'].sum()

plt.title("Question two")
barPlot = sea.barplot(sales_per_date)
barPlot.figure.set_size_inches(50,8)
plt.xticks(rotation = 90)
plt.show()