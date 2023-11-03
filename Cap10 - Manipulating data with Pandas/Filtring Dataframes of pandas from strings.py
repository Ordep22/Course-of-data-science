import pandas as pd

dataFrame = pd.read_csv("dataset.csv")

# Show head data frame

# print("Heard Data Frame\n")
# print(dataFrame.head())

'''
First, we are going to implement a method that can 
find strings that begin with som specifics characteres
'''

print("Fins elemnts tath begin with 'Con'\n")
print(dataFrame[dataFrame.Segmento.str.startswith('Con')].head())

'''
Second, we are going to implement a method that can 
find strings that end with some specific characteres
'''

print("Fins elemnts tath end with 'ice'\n")
print(dataFrame[dataFrame.Segmento.str.endswith('ice')].head())
