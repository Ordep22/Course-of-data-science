import seaborn as sea
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#Charging datasets from Seaborn library
data  = sea.load_dataset("tips")

sea.jointplot(data = data, x = "total_bill", y = "tip", kind = 'reg')

plt.show()



