import matplotlib.pyplot as plt

from libraries import  *

csvData = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/dados/dataset.csv")

dataFrame  = pd.DataFrame(csvData)

#print(dataFrame.head())

#Average sales per segment

info  = list(dataFrame['Data_Pedido'])

dataFrame.insert(2,'Ano_Pedido',"",True)

dataFrame.insert(3,'Mes_Pedido',"",True)

print(dataFrame.head())

for index in range(0,len(dataFrame['Data_Pedido']),1):

        #It`s so important to use in dayle data scienc!
        dataFrame.iat[index,2] = dataFrame['Data_Pedido'][index][6:]

        dataFrame.iat[index,3] = dataFrame['Data_Pedido'][index][3:5]

average_sales = dataFrame.groupby(['Ano_Pedido','Mes_Pedido','Segmento'])['Valor_Venda'].agg([np.sum,np.mean,np.median])


year = average_sales.index.get_level_values(0)
months  = average_sales.index.get_level_values(1)
segment  = average_sales.index.get_level_values(2)

plt.figure(figsize=(12,6))
sea.set()
fig = sea.relplot(kind = 'line', data=average_sales, y = 'mean',x = months, hue = segment, col = year, col_wrap= 4)
plt.savefig("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/RQ_9")




