from libraries import *
salesdiscount10 = 0
salesdiscount15 = 0
data  = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/dados/dataset.csv")

dataSet = pd.DataFrame(data)

#unitary_average_value_bigger_ten = dataFrame[dataFrame['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda  x: x['Unidades_Vendidas'].mean() > 10)

print(dataSet['Valor_Venda'].head())

for index in range(0,len(dataSet['Valor_Venda']),1):

    print(dataSet['Valor_Venda'][index])

    if dataSet['Valor_Venda'][index] > 1000:

        salesdiscount15 += 1


print(f"The number of sales eligible to receive a discount are: {salesdiscount15}")




