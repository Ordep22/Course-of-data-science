import matplotlib.pyplot as plt

from libraries import *

data  = pd.read_csv("dados/dataset.csv")

dataSete  = pd.DataFrame(data)

##Question five  - Which segment had the bigest sales result?##

salesResult  = dataSete.groupby('Segmento')['Valor_Venda'].sum()
img, _ = plt.pie(salesResult, radius= 1 ,labels= salesResult,explode= (0.1,0,0),center=(4,4),colors=['DarkRed', 'FireBrick', 'LightSalmon'])
plt.legend(salesResult.index, loc = "upper left")
#plt.title("Sales per Segment")
plt.savefig("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/RQ_5")













