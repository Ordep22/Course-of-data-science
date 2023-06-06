#Jason  - Java script object notation
#É um maniera de armazenar informações de forma organizada e de fácil
# acesso. Em poucas palavras, ele dá-nos uma coleção legível de dados que
#que podem ser acessadas de forma muito lógica. Pode ser uma fonte de Big Data.

import json
from urllib.request import urlopen


#Criando um dicionário
dict  = {'Nome':'Guido Van Rossum ','Linguagem':'Python','Similar':['C','Mudula-3','lisp'],'User':100000}

#Imprimindo o dicionário
for x, y in dict.items():
    print(x, y)

#Convertendo um dicionário em um arquivo json
#Basicamente a função dumps converteu o dicionário em uma única string
dictJson = json.dumps(dict)


#Criando um arquivo Json

with open ('dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict))

with  open ('dados.json', 'r') as arquivo:
    texto  = arquivo.read()
    data = json.loads(texto)

print(data)
print(data['Nome'])

#Imprimindo um arquivo jason copiado da internet

respose  = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data  = json.loads(respose)[0]

print("Título: ", data['title'])
print('URL: ',data['url'])
print('Duração ',data['duration'])
print('Número de visualizações: ',data['stats_number_of_plays'])














