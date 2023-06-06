import pandas as pd
'''
Files

Python uses file objects to interact with files on your computer.
These file objects can be any type of file such as audio, a text file, email,
Excel documents, etc.


Some most common important methods (functions) in Python
- open()           Open a file
- read()            Read a file
- Write()           Save a file
- seek()            Return to file begin
- readlines()      Return the list line file
- close()            Close file
'''

path = r"/Cap06 - Processing files, modules, packages and built-in functions/fileOne.txt"

path01 = r"/Users/PedroVitorPereira/Documents/GitHub/Python_Projects/course-of-data-science/Cap06_Processing files, modules, packages and built-in functions/salario.csv"

'''
Read files

#Neste ponto estamo abrindo o arquivo, mas ainda não realizamos nenhuma manipulação
arquivo  = open(path,"r")
print(arquivo.read())

#Com este método podemos contar a quantidade de caracteres presentes neste arquivo
print(f"O número de caracteres dentro deste arquivo é:{arquivo.tell()}")

#Caso seja necessário retornar à um ponto específico do arquivo podemos utlizar o seguinte método
#Este método funciona recebendo os parâmetros de linha e coluna (0,0) (0,0,1)
print(f"O elemento da coluna zero e linha zero é:f{arquivo.seek(0,0)}")

#Podemos ainda, especificar uma quantidade específica de caracteres que desejamos ler com o método read
#Basta passarmos um parâmetro numérico para a função read()
print(f"A leitura dos dez primeiros caracteres é: {arquivo.read(16)}")
'''


#Open file for read

fileOne  = open(path,"r") # "r" means read

print(type(fileOne))

"""
fileOne is a <class '_io.TextIOWrapper'>
It menas that is a object witch save the content of a file
"""

#Read a file save in variable fileOne and print the content
print(fileOne.read())


#Is necessary we can count the number of character of the file with method TELL
print(f"The number of character the file is: {fileOne.tell()}")


'''
Whem we read a file the cursor go to the end file. So, if you read one more time the script doesn't 
show anything.
To solution this we can use the method SEEK witch return to the init of file
'''
#Retur to init to the file
print(fileOne.seek(0,0))


#Show the limited number of character to the file
print(fileOne.read(10))

#Show the rest of character of a file
print(fileOne.read())







