import pandas as pd
import numpy as np

dataFrame  = pd.read_csv("chord-progressions.csv")

#Show the head of dataFrame
print(f"{dataFrame.head(10)}\n")

#Show the shape of dataFrame
print(f"The number of lines is:{dataFrame.shape[0]}\n")
print(f"The number of colunms is:{dataFrame.shape[1]}\n")

#find a value in the specific colunm

count  = dataFrame.count(6)

print(f"There are numbers six in the dataFrame:{count}\n")
print(dataFrame.isin([6]))











