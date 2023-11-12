import matplotlib.pyplot as plt

listOne = [1,2,5,7,9]
listTow = [7,8,2,4,2]
listThree = [2,4,6,8,10]
lisFour = [6,7,8,2,4]

#Here we can see an important characterists of the graphic plots. This is
# a way to plot some graphics one over the other.
plt.bar(listOne,listTow,label = 'Data One', color = 'green')
plt.bar(listThree,lisFour,label = 'Data Tow', color  = 'grey')
plt.legend()
plt.show()
