##Arquivos CSV são basicamente arquivos separados por virgula
# CSV - Comma Separated Values

# Para manipular arquivos CSV em Python podemos utlizar a funcão csv
import csv
import os

controle  = 0

# Abrindo o arquivo e inserindo informações

with open("numeros.csv", 'w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(("Primeira", "Segunda", "Terceira"))
    writer.writerow((50, 60, 70))
    writer.writerow((80, 90, 100))

with open("numeros.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

with open("numeros.csv", "r") as arquivo:
    for i in arquivo:
        print(i)


#print(dados)

##Estudar melhor como funciona esse With