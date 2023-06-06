##Nesta aula iremo aprender os conceitos sobre Dicionários em python

##Vejamos a diferença entre dicionários e listas
##Dicionários

#****Uma boa prática de programação é não utilizar os mesmo valores de chaves para valores

Studants_list  = ["Matheus",24,"Pedro",25,"Paulo",36]
print(Studants_list)

##Listas

Studants_dictionary = {"Matheus":24,"Pedro":25,"Paulo":36}
Studants_dictionary_01 = {"Matheus":24,"Pedro":25,"Paulo":36}
Studants_dictionary_02 = {"Maria":22,"Joana":19,"Ana":55}

print(Studants_dictionary)

'''
Repare que a principal diferença entre um dicionário e uma lista é sua contrução
Uma lista e contruida com CHAVES já um dicionário com COLCHETES 

***Os dicionários são contituidos por uma CHAVE e um valor
'''

#Neste esse exemplo queremos retornar o valor correspondente à chave Matheus

print(Studants_dictionary["Matheus"])

'''
A saída deste print é 24 o valor correspondente à chave Matheus
'''

#É possível também atribuir um novo valor à uma chave

'''
Digamos que desejamos atribuir uma nova idade à chave Matheus
Portanto, baste atribuirmos um novo valor. Da mesma maneira que fizemos com as listas
'''


Studants_dictionary["Mathues"] = 20

print(f'A idade correta de Matheus é: {Studants_dictionary["Matheus"]}')

#Podemos, também, adiocnar um novo par a um dicionário facilmnte sem o comando .append

Studants_dictionary["Bernardo"] = 36
print(Studants_dictionary)

'''
Perceba que o novo elemento foi adicionado ao fim do dicionário Studants_dictionary
{'Matheus': 24, 'Pedro': 25, 'Paulo': 36, 'Mathues': 20, 'Bernardo': 36}
'''

#Podemos também apagar os elementos de um dicionário implementanto o método clear

print(f'O dados são: {Studants_dictionary_01}')
Studants_dictionary_01.clear()
print(f'Os novos dados são: {Studants_dictionary_01}')

'''
É possível perceber que os dados eram:
-> O dados são: {'Matheus': 24, 'Pedro': 25, 'Paulo': 36}

Após implementarmos o comando .clear() obtivemos o seguinte resultado
-> Os novos dados são: {}


'''

'''
#É possível também deletar o um dicionário com o comando .del()


print(f'O dados são: {Studants_dictionary_01}')
del Studants_dictionary_01
print(f'Os novos dados são: {Studants_dictionary_01}')



Como deletamos o dicionário o compilador nos retornou com a seguinte mensagem
Traceback (most recent call last):
  File "/Users/PedroVitorPereira/Python_Projects/Analise de dados/Cap02/Estruturas_Dados_Dicionarios.py", line 74, in <module>
    print(f'Os novos dados são: {Studants_dictionary_01}')
NameError: name 'Studants_dictionary_01' is not defined
'''

##É possível verificar a quantidade de elementos de um dicionário por meio da função len()

size  = len(Studants_dictionary)

print(f'O tamanho do dicionário é: {size}')

'''
A saíada que obtivemos foi

-> O tamanho do dicionário é: 5

Como acionamos mais uma chave a nosso dicionário obtivemos o valor de 5 chaves

'''

##Podemos  estrair  somente as chaves do dicionário

keys = Studants_dictionary.keys()
print(f'As chaves do dcionário são: {keys}')
'''
As chaves do dcionário são dict_keys(['Matheus', 'Pedro', 'Paulo', 'Mathues', 'Bernardo'])
'''

##Podemos também estrair o valores das chaves deste dicionário com a função .values()

value = Studants_dictionary.values()
print(f'Os valores do dcionário são: {value}')
'''
Os valores do dcionário são dict_values([24, 25, 36, 20, 36])
'''

#Podemos ainda retornar todos os itens de um dicionário caso desejado

items  = Studants_dictionary.items()
print(f'Os itens do dicionário são: {items}')

##Podemos também "concatenar" dois dicionário com a função .update()


Studants_dictionary.update(Studants_dictionary_02)

print(f'O novo dicionário é:{Studants_dictionary}')

'''
Podemos perceber que o novo dicionário é

- >O novo dicionário é:{'Matheus': 24, 'Pedro': 25, 'Paulo': 36, 'Mathues': 20, 'Bernardo': 36, 'Maria': 22, 'Joana': 19, 'Ana': 55}

Os novos elementos foram adcionados so final do dicionário


'''

#Podemos criar um dicionário vazio

Vazio_dictionary = {}
print(f'O dicionário vazio é:{Vazio_dictionary}')

'''
-> O dicionário vazio é:{}
'''

#Vamos criar um dicionário que é composto por uma chaves e valores que são listas

Dict_dictionary = {'Nomes':["Pedro","Maria","João","Paulo"],'Estados':["MG","RJ","SP","MA"]}

##Agora vamos acessar uma determinada chave e nesta chave acessar um itens de lista
##Acessamos a chave Nomes e transformamos o item Maria e letras maúsculas MARIA

Dict_dictionary['Nomes'][1] = Dict_dictionary['Nomes'][1].upper() # O item foi substituido pelo novo valor
print(Dict_dictionary)

'''
-> {'Nomes': ['Pedro', 'MARIA', 'João', 'Paulo'], 'Estados': ['MG', 'RJ', 'SP', 'MA']}
'''


##Podemos realizar operações com os elementos de um dicionário.

Dict_Elementos  = {'Key_01':[24,25,26,27,28],'Key_02':25,'Key_03':26}

Dict_Elementos['Key_01'][0] -= 10

print(Dict_Elementos)

##É possível também utilizar dicionários aninhados

Dict_ainhado = {'Key_01':{'Key_01.1': "Dicionário aninhado em Python!!!",'Key_01.2':"É importante para DeepLearning"}}
print(Dict_ainhado['Key_01']['Key_01.1'])





















































































































