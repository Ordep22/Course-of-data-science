import pandas as pd


dataFrame  = pd.read_csv("dataset.csv")

#Calculate the mode of the value
#mode  = dataFrame["Quantidade"].value_counts().index[0]

#Put random number in the colunm
#dataFrame["Quantidade"].fillna(value= mode,inplace=True)

#Show new dataFrame
#print(dataFrame.head(10))

#Join the colunm with goup by

print(dataFrame[['Segmento','Regiao','Valor_Venda']].groupby(by=['Segmento','Regiao']).mean())
