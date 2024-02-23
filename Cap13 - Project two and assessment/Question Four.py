import matplotlib.pyplot as plt

from libraries import *

data = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/dados/dataset.csv")

dataFrame  = pd.DataFrame(data)

cities_sales = dataFrame.groupby('Cidade')['Valor_Venda'].sum()

new = cities_sales.sort_values(ascending=False)
#serie_names  = new.index
plt.figure(figsize=(13,8))
sea.barplot(new.iloc[0:10])
plt.xticks(rotation = 80)
plt.show()




