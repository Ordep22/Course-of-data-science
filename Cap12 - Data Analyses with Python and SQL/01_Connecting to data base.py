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

    #Show the informations in the data base
    data  = cursor.fetchall()

    print("Database")
    for i in data:
        print(i)
    print("\n")









except:
    print("Something went wrong!")