import os

# A biblioteca Operating System (OS) é uma das usadas para manipular arquivos em diretórios
import os

string = "Cientistas de dados é a profissão que mais tem crescido em todo " \
         "mundo.Esses profissionais precisam se especializar em progração, " \
         "estatistica e Machine Learning"

#Nesta etapa vamos usar uma abordage diferente. Será utilizado a função with
#Que, basicamente, significa
#Com o arquivo aberto como arquivo
#leia o arquivo e salve em conteudo

# with open("cientista.txt","r") as arquivo:
#     conteudo = arquivo.read()
# print("O conteudo sem formatação é:\n")
# print(conteudo)

with open("cientista.txt", "w") as arquivo:
    arquivo.write(string[:46])
    arquivo.write("\n")
    arquivo.write(string[51:])

arquivo  = open("cientista.txt", "r")
conteudo = arquivo.read()
arquivo.close()

print("O arquivo formatado é:\n")
print(conteudo)