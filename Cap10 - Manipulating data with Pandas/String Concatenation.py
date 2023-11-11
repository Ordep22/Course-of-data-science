import pandas as pd

dataFrame  = pd.read_csv("dataset.csv")

print("The head of dataFrame is:")
print(dataFrame.head())
print("\n")

#Join tow colunms ID_Pedido e Segmento

dataFrame['Pedido_Segmento'] = dataFrame['ID_Pedido'].str.cat(dataFrame['Segmento'],sep = '**')


print("The new colunm is:\n")
print(dataFrame['Pedido_Segmento'].head())
#print(dataFrame.head())
