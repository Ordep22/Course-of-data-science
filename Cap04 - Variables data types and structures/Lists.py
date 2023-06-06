'''


** Listas são a visão geral de uma string. Seus elementos podem ser mutáveis
** Elas são construidas com o usos de colchetes [] e seus elementos são separados pode vírgulas

lista = [item01,item02,item03,....intemn]

Pontos positivos

1) Listas não têm tamanho fico (Não precisamos especificar seu tamanho)

2) Listas não têm restrições de tipo fixo

3) É possível criar listas aninhadas mas, o que isso quer dizer? É possível criar uma lista dentro de outra lista

'''

Lista_Compras_01 = ["ovos,banana,farinha,aveia,carnes"] ##Uma Lista contendo uma única string com várias informações
print(f'{Lista_Compras_01}\n')


Lista_Compras_02 = ["Ovos","Frutas","Leite","Carnes","aveia"] ##Uma lista contendo várias informações com strings distintas
print(f'{Lista_Compras_02}')

##Acessando os elemtos de umas listas

print(f'{Lista_Compras_02[0]}')

##As listas não possuen restrição de tipo, ou seja eles são capazes de armazenar variáveis do tipo int, char, bool...

Lista_Compras_03 = ["Ovos",12,"Carnes",3]
print(f'{Lista_Compras_03}')

##Atribuido cada valor a da lista a uma variavel

item1 = Lista_Compras_03[0]
item2 = Lista_Compras_03[1]
item3 = Lista_Compras_03[2]

print(item1,item2,item3)


##Podemos também atualizar um item da lista
##Ao contrário de uma string a lista é mutável e podemos alterar seus elementos

Lista_Compras_03[1] = "Frutas"
Lista_Compras_03[2] = "Leite"
Lista_Compras_03[3] = "Carnes"

#Antiga Lista de compras 3
#Lista_Compras_03 = ["Ovos",12,"Carnes",3]

#Nova Lista de compra
print(f'{Lista_Compras_03}')

##É possível deleter um item que está contido na lista

del Lista_Compras_03[0]
print(f'{Lista_Compras_03}')
#Como podemos perceber o item "Ovos" foi deletado da lista.


##Podemos criar uma lista de listas
##Podem ser chamadas de listas aninhadas

Lista = [[1,2,3],[4,5,6],[7,8,9]]

#Imprimindo o item '0' da lista Lista

Elemento_Lista  = Lista[0]
#Elemento_Lista = [1,2,3]

print(Elemento_Lista)

#Acessando os elementos contidos no item zero da lista
print(f'{Elemento_Lista[0]}\n')
print(f'{Elemento_Lista[1]}\n')
print(f'{Elemento_Lista[2]}\n')

##Podemos também concatenas listas

Lista_00 = Lista[0]+Lista[2]
print(f'Lista_00:\n{Lista_00}')


##Opreador IN, podemos realizar uma pesquisa com esse operador.
##Essse operador é muito importante pois podemos buscar alguns elementos em lista enormes

if ((1 in Lista_00)):

    print("O numero 1 está contido a lista")


else:
    print("O numero 100 não está contido")

##Funções built in

#Retorna o tamanho da lista

print(f"O tamanho da lista é: {len(Lista_00)}")

#Função MAX() retorna o valor máximo da lista

print(f"O maior valor da lista é: {max(Lista_00)}")

#Função MIN() retorna o valor minimo da lista

print(f"O maior valor da lista é: {min(Lista_00)}")


#É possível também adcionar novos elementos à lista com um função built-in

Lista_00.extend([10,11])

print(f"A lista extendida é: {Lista_00}")


#Adicionando um elemento à lista

Lista_00.append(-1)
print(f"A nova lista é: {Lista_00}\n")


Nova_Lista  = []

for i in Lista_00:
    Nova_Lista.append(i+1)

print("A nova lista com o acressimo de uma unidade é:")
print(Nova_Lista)



#Função para obter o elemento um elemento da lista

index_aveia  = Lista_Compras_02.index("aveia")
print(f"O indice de aveia é: {index_aveia}")

#Ao contrário da função .append() podemos incerir um elemento em uma parte específica da lista com a função .insert()

Lista_Compras_02.insert(0,"Legumes")
print("A nova lista de comprar é:\n")
print(Lista_Compras_02)

#É possível também inverter a lista usando a função .reverce() --> Parece não estar diponível no Python 3.8

#É possível também ordenar a lista com a função .sort() --> parece não estar funcionando no Python 3.8

print(f"A lista ordena é: {Nova_Lista.sort()}")






























































































