import matplotlib.pyplot as plt

from libraries import *

data = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/dados/dataset.csv")

dataFrame  = pd.DataFrame(data)

cities_sales = dataFrame.groupby('Cidade')['Valor_Venda'].sum()



new = cities_sales.sort_values(ascending=False)
#serie_names  = new.index
plt.figure(figsize=(16,8))
sea.set_palette('coolwarm')
sea.barplot(new.head(10)) #iloc is not recomendaded
plt.xticks(rotation = 50)
plt.show()




