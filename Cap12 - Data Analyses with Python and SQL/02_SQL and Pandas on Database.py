import pandas as pd
import sqlite3 as sq


#Opening conection with database
conection  = sq.connect('cap12_dsa.db')

#Opening the cursor to walk on to the database
cursor  = conection.cursor()

#Criating the first query
firstQuery  = 'SELECT * FROM tb_vendas_dsa'

#Executting the first query
cursor.execute(firstQuery)

#Return the data from execution query
data  = cursor.fetchall()

#Show database
for item in data:
    print(item)

#Transforming the database in a data frame with pandas
dataFrame  = pd.DataFrame(data, columns= ['ID_Pedido','ID_Cliente','Nome_Produto','Valor_Unitario','Unidades_Vendidas','Custo'])

#Show the data frame head
print(dataFrame.head())

cursor.close()
conection.close()

#Calculating the averege from colunm Unidades_Vendidas
average  = dataFrame['Unidades_Vendidas'].mean()

print(average)

#Appling the conditionals into "query" to calculate the average if the values is bigger than 199
unitary_average_value = dataFrame[dataFrame['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()

print(unitary_average_value)


#Check into the last resul who's bigger than 10
unitary_average_value_bigger_ten = dataFrame[dataFrame['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda  x: x['Unidades_Vendidas'].mean() > 10)

print(unitary_average_value_bigger_ten)





















