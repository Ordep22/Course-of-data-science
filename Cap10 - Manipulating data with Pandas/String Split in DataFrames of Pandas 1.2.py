import pandas as pd
print("Reading dataset...\n")
dataFrame  = pd.read_csv("dataset.csv")
print("Show head of dataset\n")
print(dataFrame.head())
print(f"The type of dataset is: {type(dataFrame)}\n")



#I need to show a head form a specif colunm
print("Head of colunm ID_Pedido\n")
print(dataFrame['Data_Pedido'].head())
print("\n")

print("Apply Lstrip in the Colunm Id_Pedidos")
print(dataFrame['Data_Pedido'].str.lstrip('20'))
print("\n")



