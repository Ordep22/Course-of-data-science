import matplotlib.pyplot as plt

from libraries import *
years  = ['2015','2016','2017','2018']
data = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/dados/dataset.csv")
dataFrame = pd.DataFrame(data)

for index in range(0,len(dataFrame['Data_Pedido']),1):

    dataFrame.loc[index, 'Data_Pedido'] = dataFrame['Data_Pedido'][index][6:]

print(dataFrame.head())

total  = dataFrame.groupby(['Segmento', 'Data_Pedido'])['Valor_Venda'].sum()

fig, axes = plt.subplots(1, 3, figsize=(25, 6))
fig.suptitle('Sales per year and segment')

# Bulbasaur
sea.barplot(data = total['Consumer'],ax=axes[0])
axes[0].set_title("Consumer Sales")


# Charmander
sea.barplot(data = total['Home Office'],ax=axes[1])
axes[1].set_title("Home Office Sales")

# Squirtle
sea.barplot(data = total['Corporate'],ax=axes[2])
axes[2].set_title("Corporate Sales")
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)

plt.savefig("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/RQ_6")
#plt.show()



