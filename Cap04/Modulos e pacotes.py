#Importando módulos em python
import math
import random
import  statistics
import urllib.request

# print("Os métodos disponíveis para o pacote Math são:\n ")
# print(dir(math))

#Usando o método sqrt do pacote Math
num  = 25
raizNum = math.sqrt(num)


#Usano o método choice do pacote random
lista  = ["Pedro","Ana","Maria","Leonardo","Ester"]
nomeSelecionado  = random.choice(lista)
print(f"O nome selecionado aleatoriamente foi: {nomeSelecionado}")
print(50*"--")

#Usando o método média do pacote statistics

dados  = [1.005,2.080979,5.09870970,7.0980789756]
media = statistics.mean(dados)
print(f"A média dos dados é:{media}")
print(50*"--")

#Usando o método request do módulo urlib

url = urllib.request.urlopen('https://www.youtube.com/watch?v=5vSyylPPEko')

print(f"A respota da URL informada é: {url}")

#Chamando o método read() do objeto e armazenando o código HTML na variável
html =  url.read()

#Mostrando o resultado
print(html)








