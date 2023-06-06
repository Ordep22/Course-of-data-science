''''
Regular expressions

[PT]

Expressões Regulares são uma sequência de caracteres que definem uma
busca padrão em strings. Em Python, as Expressões Regulares são
suportadas pelo pacotere. Ele fornece uma série de funções para pesquisar
e substituir padrões em strings. Algumas das tarefas mais comuns que
podem ser realizadas com Expressões Regulares incluem verificar se uma
string corresponde a um determinado padrão, extrair informações de uma
string combase em um padrão específico e substituir trechos de uma string
com base em um padrão.



[EN]

Regular Expressions are a sequence of characters that define a
standard search in strings. In Python, Regular Expressions are
supported by the package. It provides a number of functions to search
and replace patterns in strings. Some of the most common tasks that
can be performed with Regular Expressions include checking whether a
string matches a given pattern, extract information from a
string based on a specific pattern and replace chunks of a string
based on a pattern.



'''
import re
##Regex with ChatGPT
##New concept: whem we use tree simple asps in the stard and end of
## the strin it's Doc String

article  =  ''' IA que significa inteligência artificial refere-se a sistemas ou 
máquinas que mimetizam a inteligência humana para executar tarefas e 
podem se aprimorar iterativamente com base nas informações que eles 
coletam. A IA se manifesta de várias formas'''


#Task one
##Find out how many time the character 'a' appears in the docstring


#REGEX solution
aApperars = len(re.findall("a",article))
print(f" The character 'a' appears {aApperars}  time.")



#Task tow




















