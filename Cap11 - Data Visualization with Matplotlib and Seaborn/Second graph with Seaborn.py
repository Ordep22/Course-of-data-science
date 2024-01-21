import seaborn as sea
from matplotlib import pyplot as plt


data  = sea.load_dataset("tips")

#print(data.head())

sea.lmplot(data = data, x = "total_bill", y = "tip", col  = "smoker")

plt.show()