# A biblioteca Operating System (OS) é uma das usadas para manipular arquivos em diretórios
import os

string = "Cientistas de dados é a profissão que mais tem crescido em todo mundo." \
         "Esses profissionais precisam se especializar em progração, estatistica e Machine Learning"

# Abrindo o arquivo com os parâmetro da biblioteca OS
arquivo = open(os.path.join("cientista.txt"), "w")

##Gravando os dados no arquivo
for palavra in string.split():
    arquivo.write(palavra + " ")

# Fechar o arquivo após a gravação das informações
arquivo.close()

##Lndo as informações do arquivo e imprimindo

# Abrindo o arquivo
arquivo = open("cientista.txt", "r")

# Lendo o que está contiido no arquivo
conteudo = arquivo.read()

# Fechando o arquivo
arquivo.close()

# Imprimindo o conteudo do arquivo lido
print(conteudo)
