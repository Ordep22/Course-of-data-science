import pandas as pd

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

        dataFrame['Ano_Pedido'][index] = dataFrame['Data_Pedido'][index][6:]

        dataFrame['Mes_Pedido'][index] = dataFrame['Data_Pedido'][index][3:5]



average_sales_year = dataFrame.groupby(['Ano_Pedido','Segmento'])['Valor_Venda'].mean()

average_sales_month = dataFrame.groupby(['Mes_Pedido','Segmento'])['Valor_Venda'].mean()

print(average_sales_month)

