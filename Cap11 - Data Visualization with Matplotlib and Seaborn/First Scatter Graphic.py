import matplotlib.pyplot as plt

listOne = [1,2,3,4,5,6,7,8]
listTow = [5,2,4,5,6,8,4,8]

plt.scatter(listOne,listTow,label = 'Pontos', color = 'red',marker= 'o')
plt.legend()
plt.show()

