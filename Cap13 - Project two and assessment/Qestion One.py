from libraries import *

# Read database
dataBase = pd.read_csv(
    "/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/dados/dataset.csv")

dataFrame = pd.DataFrame(dataBase)

#Exploration Analyses

##Coluns of data sate
print(dataFrame.columns)
print('\n')

##Verifying data type from coluns
print(dataFrame.dtypes)
print("\n")

##Verifying if there are any duplicate values
print(dataFrame[dataFrame.duplicated()])
print("\n")

##Statisc resume form sales value colum
print(dataFrame['Valor_Venda'].describe())
print('\n')

##Verifying if there are any null values
print(dataFrame.isnull().sum())
print('\n')

# Show the head of data base
print(dataFrame.head())

# Show tail of data base
print(dataFrame.tail())

print(40*"--")
print('Starting Project Solution')
print(40*"--")
print('\n')


print(15*"--" + ' Q1 ' + 15*"--")
print("Which cyte has the highest sales value in the 'Office Supplies' product category?")
print(30*"--")

#print(sales_per_city.head())

# --> Agrouping the
sales_per_product = dataFrame[dataFrame['Categoria'] == 'Office Supplies'].groupby(['Cidade'])['Valor_Venda'].sum()

print(f"{sales_per_product.idxmax()} --> {sales_per_product.max()}")


#print(sales_per_product.sort_values(ascending=False))