import sqlite3 as sq
import pandas as pd
try:
    #Connect to SQL server
    '''
        It's a way to connect to sqlite server. If it's necessary to connect  to another one you 
        have to search a specific function to do this
    '''
    dataBase = sq.connect("cap12_dsa.db")
    print("Connected\n")

    #Set the cursor position
    cursor = dataBase.cursor()

    #Query SQL to extract informations
    sqlQuery  = """ SELECT name FROM sqlite_master WHERE type  = 'table' """

    #Execute a Query
    cursor.execute(sqlQuery)

    #Visualising resuts
    print("Data base")
    print(cursor.fetchall())
    print("\n")

    #Execute the query to select all informations in tb_vendas_dsa
    sqlQuerySelect = 'SELECT *FROM tb_vendas_dsa'

    #At the conection execut the query
    cursor.execute(sqlQuerySelect)

    #Find the metadatas in the database
    colunmsName  = [ description[0] for description in cursor.description]

    print("Metadata")
    print(colunmsName)
    print("\n")

    #Show the informations in the database
    data  = cursor.fetchall()

    print("Database")
    for i in data:
        print(i)
    print("\n")

    #Creating the Query to calculate the average of sales unite
    salesQuery  = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'

    #Execute the query on database
    resultAvg = cursor.execute(salesQuery)

    print("The average of sales unite is:")
    print(resultAvg.fetchall())
    print("\n")


    #Creating the Query that it'll select the average from the sales products
    productsAVGQuery = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'

    #Execute the last query
    result_productsAVGQuery = cursor.execute(productsAVGQuery)

    #Show the result of the execution
    print("The avarage from the sales product is:")

    for item in result_productsAVGQuery.fetchall():
        print(item)
    print("\n")


    #Creating the Query that it'll filter the product sales value whem it was biger them 199

    filterQuerry  = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa WHERE Valor_Unitario > 199 GROUP BY Nome_Produto'

    resultFilter = cursor.execute(filterQuerry)

    for item in resultFilter.fetchall():

        print(item)

    print("\n")



    filterQuerry_2 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa WHERE Valor_Unitario > 199 GROUP BY Nome_Produto HAVING AVG(Unidades_Vendidas) > 10 '

    resultFilter_2 = cursor.execute(filterQuerry_2)

    for item in resultFilter_2:
        print(item)

    print('\n')








    cursor.close()
    dataBase.close()












except:

    print("Something went wrong!")