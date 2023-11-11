import pandas as pd

dataFrame  = pd.read_csv("dataset.csv")

#Show the head data frame
print("The head of data frame is:")
print(dataFrame['ID_Cliente'].head())
print("\n")

#Chagind characters in a colunm in a dataframe
dataFrame['ID_Cliente'] = dataFrame['ID_Cliente'].str.replace('CG','AX')

#Show the dataframe with the new chages
print("The colunm ID_Cliente is:\n")
print(dataFrame['ID_Cliente'].head())


