import matplotlib.pyplot as plt
from pylab import *

"""
[PT-BR]
Gráfico de linha é um tipo de plotagem usado para representar a evolução do comportamento de 
uma varábel com diferntes pontos de dados. O gráfico normalmente é usado com variáveis contínuas.
No gráfico de linha, cada ponto de dados é representados por um ponto na linha. A linha concta os pontos de dados. 
Os gráficos de linha são úteis para visualizar tendência e padrões em dados contínuos ao longo do tempo. Por exemeplo, 
eles podem ser usados paramostrar a variação da temperatura ao longo de um período de 
tempo, e evelucão da populacão em uma região ou flutuação do valor de uma ação na bolsa de valores 


"""

#Data
x = linspace(0,5,10)
y = x ** 2

#Criate a figure
figure  =  plt.figure()

#Define axes scale
axes  = figure.add_axes([0.14,0.14,0.8,0.8])

#Criate plot
axes.plot(x,y,'r')

#Labels and title
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title("Line Graphic")

"""
Whem we going to use PyLab we have to use plt.show() to show the graphic
"""
plt.show()









