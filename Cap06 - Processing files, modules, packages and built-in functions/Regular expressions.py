''''
Regular expressions

[PT]

Expressões Regulares são uma sequência de caracteres que definem uma
busca padrão em strings. Em Python, as Expressões Regulares são
suportadas pelo pacotere RE. Ele fornece uma série de funções para pesquisar
e substituir padrões em strings. Algumas das tarefas mais comuns que
podem ser realizadas com Expressões Regulares incluem verificar se uma
string corresponde a um determinado padrão, extrair informações de uma
string combase em um padrão específico e substituir trechos de uma string
com base em um padrão.



[EN]

Regular Expressions are a sequence of characters that define a
standard search in strings. In Python, Regular Expressions are
supported by the package RE. It provides a number of functions to search
and replace patterns in strings. Some of the most common tasks that
can be performed with Regular Expressions include checking whether a
string matches a given pattern, extract information from a
string based on a specific pattern and replace chunks of a string
based on a pattern.



'''

# re = Regular expressions
import re

recorrencia  = 0

## Efficient way
text = "Meu e-mail é nome@empresa.com.br e você pode me contactar em outronome@empresa.com.br"

resultado  = len(re.findall("@",text))

print(f"O caracter @ foi identificado {resultado} vezes na fraze!")

## Inefficient way
for i in text:

    if i == "@":
        recorrencia  += 1

print(f"O caracter @ foi identificado {recorrencia} vezes na fraze!")


#Find the next word

nextWord  = re.findall(r" você (\w+) ",text)

if nextWord[0] != "":
    print(f"The next word afeter 'você' is: {nextWord[0]}")
else:
    print("Não foi possível encontrar a palavra desejada!")