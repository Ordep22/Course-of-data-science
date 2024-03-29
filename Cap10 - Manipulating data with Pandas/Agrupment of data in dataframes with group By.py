import pandas as pd


dataFrame  = pd.read_csv("dataset.csv")

#Calculate the mode of the value
#mode  = dataFrame["Quantidade"].value_counts().index[0]

#Put random number in the colunm
#dataFrame["Quantidade"].fillna(value= mode,inplace=True)

#Show new dataFrame
#print(dataFrame.head(10))

#Join the colunm with goup by
print("Whith Groupby\n")
print(dataFrame[['Segmento','Regiao','Valor_Venda']].groupby(by=['Segmento','Regiao']).mean())

print("\n\n")

print("Whith Groupby and AGG\n")
print(dataFrame[['Segmento','Regiao','Valor_Venda']].groupby(by =['Segmento','Regiao']).agg(['mean','std','count']))