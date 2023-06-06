'''
1) As strings são utlizadas para gravar informações em fomato de texto

String  - sequencia imutável de caracteres ou apenas 1 caracter
    -> "Essa é uma string"
    -> "a"

2) Os componentes de um string podem ser acessados por indices

texto = "Python para análise de dados"  ou
texto  = 'Python para análise de dados'

***Em python podemos utlizar a delclração de strings com aspas simples ou aspas duplas

texto[0] = P
texto[1]  = y

3) Funções Built-In de Strings

Python é uma linguagem orientada a objeto, sendo assim as estruturas de dados possuen atributos
(propriedade) e métodos (rotinas associadas às propriedade). Tando os atributos quanto os métodos são acessados usando
ponto (.)

Os métodos estão sob a forma:

    objeto.atributo
    objeto.metodo()
    objeto.metodo(parametro)



'''

string = "Python para análise de dados"

print("----------------------------------------")
print("O primeiro elemento da string é:")
print(string[0])
print("----------------------------------------")

## Podemos também utlizar o slice para fazer o fatiamento da stringo por meio dos dois ponto

'''
sring[x:Y]
    -> X representa a posição inicial o fatiamento 
    -> Y representa a posição final do fatiamento
'''

print("----------------------------------------")
print("Os elementos de zero até 5 são:")
print(string[:5])
print("----------------------------------------")

#podemos também acessar a string de traz para frente utlizando os caracteres negativos

print("----------------------------------------")
print("O ultimo elemento da string é:")
print(string[-1])
print("----------------------------------------")

#Podemos também trabalhar com vetores pulando linhas
#Utilizando a seguinte notação
#O mesmo pode ser feito usando a notação negativa

print("----------------------------------------")
print("Saltando elementos em um vetor")
print(string[::2])
print("----------------------------------------")

# Alterando um caracter (não é possível um elemento da string)
try:

    string[0] = "O"

except:

    print("----------------------------------------")
    print("Não é possível alterar um único elemento da string sem modificar seu tipo")
    print("----------------------------------------")



#É possível também realizar a concatenação de strings
#Utilizando o sinal de + (mais) entre as strings

s_01 = "Hi, my name is Pedro!"

s_02 = "Today, we going to learn about strings in python"

s_03 = s_01+s_02
print(s_03)

#Funções Built-in de strings

frase = "Let`s to code my friends!"


#Upper case
print(frase.upper())
print("\n")


#Lower Case
print(frase.lower())
print("\n")

#Dividir uma string por espaços em branco
print(frase.split()) ## Split  -> Do inglês Dividir
print("\n")

#Dividir uma string por um elemento específico
print(frase.split("e"))
print("\n")

#Funções de Strings

s_04 = "there are many functions but, somthings are moste usualy!"

#capitalize -> Torna a primeira letra maiusculo

print("\n")
print(s_04.capitalize())

#count -> conta a recorrência de uma determinado caracter em uma string

print("\n")
print(f"O caracter 'e' aparece {s_04.count('e')} vezes")

#finde -> verifica em qual posição ocorre a aprição de um determinado caracter

print("\n")
print(f"O caracter 'y' apareceu pela primeira vez na posição  {s_04.find('y')}")

#.lower -> verifica se o caracter é um espaço

print("\n")
print(f"O caracter é um espaço {s_04.isspace()}")

#.endswith verifica se a string termina com um determinado caracter

print("\n")
print(f"A string finaliza com o caracter '!'? {s_04.endswith('!')}")


#Metodos comparativos
#Nos podemos comparar elemtros ou strings completas

print("\n")

print(f"'Python' == 'python'? {'Python' == 'python'}")















































































































