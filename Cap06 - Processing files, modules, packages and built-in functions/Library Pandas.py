import pandas as pd

#Path for file
file  = r"/Cap06 - Processing files, modules, packages and built-in functions/salario.csv"

#Read a file from path
df = pd.read_csv(file)

#Print head of a file
print(df.head())

#print(df["Position Tile"].value_counts())

