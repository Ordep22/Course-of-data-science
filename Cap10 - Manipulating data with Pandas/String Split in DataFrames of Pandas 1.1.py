import pandas as pd
print("Reading dataset...\n")
dataFrame  = pd.read_csv("dataset.csv")
print("Show head of dataset\n")
print(dataFrame.head())
print(f"The type of dataset is: {type(dataFrame)}\n")



#I need to show a head form a specif colunm
print("Head of colunm ID_Pedido\n")
print(dataFrame['ID_Pedido'].head())
print("\n")

print("Spliting Colunm Id_Pedidos from year")
newList = dataFrame['ID_Pedido'].str.split('-')
print("\n")

print("To get year from string")
clunmYear = newList.str[1].head()
print(clunmYear)
print("\n")

print("Crate a new colunm in the dataSete!\n")
dataFrame['Ano'] = clunmYear
print("\n")

print("Show the new dataFrame!\n")
print(dataFrame.head())


