import pandas as pd
'''
Arquivos

Python usa objetos de arquivos para interagir com arquivos em seu computador.
Esses objetos de arquivos podem ser qualquer tipo de arquivos como áudio, um arquivo de texto, e-mail,
documentos do Excel, etc.

Alguns métodos (funções) importantes mais usuais no Python
 - open()           Abre um arquivo
 - read()            Usado para ler um arquivo
 - Write()           Usado para gravar o arquivo
 - seek()            Retorna para o início do arquivo
 - readlines()      Retorna a lista de linhas do arquivo
 - close()            Fecha o arquivo
'''

path = r"/Users/PedroVitorPereira/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/Projetos-Python/Analise de dados/Cap04/arquivo_01.txt"
path01 = r"/Users/PedroVitorPereira/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/Projetos-Python/Analise de dados/Cap04/salario.csv"

'''
Leitura de arquivos



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


'''
Escrita de arquivos
'''
#Para podermos obreescrever um arquivo basta passamos o parâmetro w para a função open()
#Esse métodos apaga as informações anteriores e escreve as novas informações em  no arquivo

# arquivo = open(path,"w")
# arquivo.write("Escrevendo alguma informação no arquivo.")
# arquivo = open(path,"r")
# print(arquivo.read())


##Trabalhando com base de dados
#Data set é um conjunto de dados

#Abre o arquivo CSV em modo de leitura
#f = open('salario.csv','r')


##Abrindo e dividindo os arquivos por espaços vazios ao final de cada linha
# data  = f.read() # Executa a ação de ler o arquivo
# rows  = data.split('\n') #Divide o arquivo por espaços ao final da linha (enter do teclado) quebra por linhas
# print(rows) # printa as colunas separadas por espaços

##Arbindo e dividindo o arquivo por linhas

# data = f.read()
# rows = data.split('\n')
#
# full_data = []
#
# for row in rows:
#     split_row = row.split(",")
#     full_data.append(spli_row)
#
# print(full_data)


##Contando as linhas de um arquivo

# f = open('salario.csv','r')
# data = f.read()
# rows = data.split('\n')
#
# full_data  = []
# cont = 0
# for row in rows:
#     split_row = row.split(',')
#     full_data .append(split_row)
#     cont += 1
# print(f"O número de linhas do arquivo é: {cont}")

##Contando o número de colunas de um arquivo

# f = open('salario.csv','r')
# data = f.read()
# rows = data.split('\n')
#
# full_data  = []
#
# for row in rows:
#     split_row = row.split(',')
#     full_data.append(split_row)
#
# colunas  = len(full_data[0])
#
# print(f'O numero de colunas do arquivo é {colunas}')


arquivoTxt = open(path,'r')

#Para no fim do arquvo
arquivoTxt.read()

#Retorna ao inicio do arquivo
arquivoTxt.seek(0)


#Lendo cada linha do arquivo
for i in open(path):
    print(i)

'''
Basicamente a diferenção entre os dois métodos é

Neste método, ao abrir o arquivo o Python irá ler cada elemento do arquivo e informir
(bem e não é isso que queremos)
for i in arquivoTxt.read():
    print(i)

Já nese método, o mais adequado, estamos percorrendo as linhas do arquivo
for i in open(path):
    print(i)
'''

#Importando arquivos com Pandas

csvSalario  = path01


df = pd.read_csv(csvSalario)
#O método head busca somente as primeiras linhas do arquivo que está sendo manipulado

cabecalho = df.head()
print(cabecalho)









































