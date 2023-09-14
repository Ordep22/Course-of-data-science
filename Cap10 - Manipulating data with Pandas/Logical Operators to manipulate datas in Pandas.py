import pandas as pd
import numpy as np

#Import Data frame
dataFrame  = pd.read_csv("chord-progressions.csv")

#Show head of the data frame
print("Old dataFrame\n")
print(f"{dataFrame}\n")

#Calculate the mode of the value
mode  = dataFrame["Fourth_chord"].value_counts().index[0]

#Pul random number in the colunm
dataFrame["Fourth_chord"].fillna(value= mode,inplace=True)

#Show all new data frame
print(f"{dataFrame}\n")

#Filter an specific value on the colunm
# ->>>>Tip whem we goig to contruct a csv file don't use numeber in the columns names. It's not a good job!

''' head() -> Return the fisrt values from the data set '''
print(dataFrame[(dataFrame.Fourth_chord == 5.0) & (dataFrame.Second_chord == 4.0)].head())
print("\n")

''' tail() -> Return the last values from the data set '''
print(dataFrame[(dataFrame.Fourth_chord == 5.0) | (dataFrame.Second_chord == 4.0)].tail())
print("\n")

''' sample(x) -> Return a result with  x values from the datasete'''
print(dataFrame[(dataFrame.Fourth_chord != 5.0) | (dataFrame.Second_chord != 4.0)].sample(5))
print("\n")






