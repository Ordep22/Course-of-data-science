import matplotlib.pyplot as plt

from libraries import *

csvData = pd.read_csv("/Users/PedroVitorPereira/Documents/"
                   "GitHub/Course-of-data-science/Cap13 - Project "
                   "two and assessment/dados/dataset.csv")

dataFrame = pd.DataFrame(csvData)

best_category_sales  = dataFrame.groupby(['Categoria','SubCategoria']).sum(numeric_only = True).sort_values("Valor_Venda", ascending = False).head(12)

best_category_sales = best_category_sales[['Valor_Venda']].astype(int).sort_values(by  = 'Categoria').reset_index()

#print(best_category_sales)

best_category_sales_category = dataFrame.groupby('Categoria').sum(numeric_only = True).reset_index()

print(best_category_sales_category)

main_colors = ['#FF0000', '#00FF00', '#0000FF']

secondary_colors  = ['#FF0000', '#00FF00', '#0000FF',
                                    '#FF0001', '#00FF01', '#0001FF',
                                    '#FF0002', '#00FF02', '#0002FF',
                                    '#FF0003', '#00FF03', '#0003FF',
]

plotOne  = plt.pie(best_category_sales_category['Valor_Venda'],
                   radius = 1,
                   labels = best_category_sales_category['Categoria'],
                   wedgeprops = dict(edgecolor = 'white'),
                   colors = main_colors)

plotTwo = plt.pie(best_category_sales['Valor_Venda'],
                   radius=0.9,
                   #autopct=autopct_format(best_category_sales['Valor_Venda']),  # Assuming autopct_format is correctly defined
                   colors=secondary_colors,  # Assuming secondary_colors is correctly defined
                   labeldistance=0.7,
                   labels=best_category_sales['SubCategoria'],
                   wedgeprops=dict(edgecolor='white'),
                   pctdistance=0.53,
                   rotatelabels=True)


circleCenter  = plt.Circle((0,0),0.6,fc = 'white')

fig = plt.gcf()
fig.gca().add_artist(circleCenter)
plt.annotate(text= 'Total de Vendas:'+'$'+str(int(sum(best_category_sales['Valor_Venda']))),xy = (-0.2,0))
plt.title("Top 12 sales per category")
plt.savefig("/Users/PedroVitorPereira/Documents/GitHub/Course-of-data-science/Cap13 - Project two and assessment/RQ10")