

from libraries import *

data = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/dados/dataset.csv")
dataFrame = pd.DataFrame(data)

element = dataFrame['Data_Pedido'][:][6:]

print(element.head())



#newDateframe  = dataFrame.groupby(['Data_Pedido','Segmento'])['Valor_Venda'].sum()




