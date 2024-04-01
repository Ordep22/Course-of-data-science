import matplotlib.pyplot as plt

from libraries import *

data  = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/dados/dataset.csv")
dataFrame  = pd.DataFrame(data)


print('\n')
print(15*"--" + ' Q3 ' + 15*"--")
print("Calculate the total of sales per state")
print(30*"--")

total_sale_per_state = dataFrame.groupby('Estado')['Valor_Venda'].sum()
#print(total_sale_per_state)
plt.figure(figsize=(13,8))
barPlot  = sea.barplot(data = total_sale_per_state , legend = "auto").set(title = "Total of sales per state")
#barPlot.figure.set_size_inches(20,8)
plt.xticks(rotation = 80)
plt.show()




