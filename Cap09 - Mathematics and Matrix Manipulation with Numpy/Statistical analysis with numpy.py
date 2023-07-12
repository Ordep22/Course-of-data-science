import numpy as np


#Criating an array with numpy

arrayOne  =  np.array([15,20,18,63,94,75])

#Calculating the average of this array

'''
[PT-BR]

MÉDIA
A média (Me) é calculada somando-se todos os valores de um conjunto de dados e dividindo-se pelo número de elementos deste 
conjunto. Como a média é uma medida sensível aos valores da amostra, é mais adequada para situações em que os dados são 
distribuídos mais ou menos de forma uniforme, ou seja, valores sem grandes discrepâncias.

DESVIO PADRÃO
O desvio padrão é uma medida que expressa o grau de dispersão de um conjunto de dados. Ou seja, o desvio padrão indica o 
quanto um conjunto de dados é uniforme. Quanto mais próximo de 0 for o desvio padrão, mais homogêneo são os dados.


VARIÂNCIA
Dado um conjunto de dados, a variância é uma medida de dispersão que mostra o quão distante cada valor desse conjunto
está do valor central (médio).Veja mais sobre "Medidas de dispersão: variância e desvio padrão

A viriância é um medida quadrática e pod ser útil para calcular outras estatísticas, geralmente maiores do que os valores
próprios dados, o que pode dificultar a interpretação. O desvio padrão é a raiz quadrada da variânci e fornce a interpretação 
que tem a mesma unidade de medida que os próprio dados, facilitando a interpretação e comparaçã com outros valoes

Em geral, o desvio padrão é mais comultmente usado do que a variânci , pricipamlmente porque é mais fácil de interpretar. Em alguns casos, a variância 
pode ser uma medida mais apropriada, como quando se pretende calcular outras estatísticas, como a covariência ou coeficiente. 
Em outros casos, o desvio padrão pode ser uma medida mais apropriada, como quando se pretende avaliar a consistência dos 
dados em relação à média e comparar diferentes conjuntos de dados.



[EN]

AVERAGE
The mean (Me) is calculated by summing all the values of a data set and dividing by the number of elements in this
to define. Because the mean is a measure that is sensitive to sample values, it is best suited for situations where data are
distributed more or less uniformly, that is, values of major discrepancies.

STANDARD DEVIATION
The standard deviation is a measure that expresses the degree of dispersion of a data set. That is, the standard deviation indicates the
how uniform a dataset is. The closer the standard deviation is to 0, the more homogeneous the data.


VARIANCE
Given a set of data, variance is a measure of dispersion that shows the distance between each value in that set.
is of the central value (mean). See more in "Measures of Dispersion: Variance and Standard Deviation





'''


print(f"The average of the arrayOne is: {arrayOne.mean()}\n")

print(f"The standart deviation of the arrayOne is: {arrayOne.std():.2f}\n")

print(f"The variance  of the arrayOne is: {arrayOne.var():.2f}\n")