import numpy as np

from libraries import *

salesList = []

data = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/dados/dataset.csv")

dataFrame  =  pd.DataFrame(data)

print(dataFrame.head())

for index in range(0,len(dataFrame['Valor_Venda']),1):

    if dataFrame['Valor_Venda'][index] > 1000:

        salesList.append(dataFrame['Valor_Venda'][index])

arraySales = np.array(salesList)

arraySalesbeforeDiscout = map(lambda x: x*0.85,salesList)

arraySalesbeforeDiscout = np.array(list(arraySalesbeforeDiscout))

print(f'The mean values before discount is: $ {arraySales.mean()}')

print(f'The mean values after discount is: $ {arraySalesbeforeDiscout.mean()}')




