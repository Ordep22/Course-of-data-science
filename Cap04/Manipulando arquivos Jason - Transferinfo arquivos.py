import json
import os


arquivoFonte = "/Users/PedroVitorPereira/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/Projetos-Python/Analise de dados/Cap04/dados.json"

arquivoDestino = "/Users/PedroVitorPereira/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/Projetos-Python/Analise de dados/Cap04/Data.txt"


#Método um de escrever em um arquivo
with open(arquivoFonte,'r') as inFile:
    text = inFile.read()
    with open(arquivoDestino,"w") as outFile:
        outFile.write(text)

#Mostrando os dados que foram escritos no arquivo
with open(arquivoDestino,'r') as dados:
    for i in dados:
        print(i)



#Método dois de escrever em um arquivo
#Muito mais simples
open(arquivoDestino,'w').write(open(arquivoFonte,'r').read())


#Leitura do arquivo Jason
with open(arquivoDestino,'r') as dados1:
    texto = dados1.read()
    data = json.loads(texto)

print(data)

















