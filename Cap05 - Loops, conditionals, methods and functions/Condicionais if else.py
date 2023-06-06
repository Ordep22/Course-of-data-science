##Condicionais
'''
Os condicionais if nos permite dizer ao computador para executar ações com base
em um determinado conjunto de resultados
Verbalmente, podemos imaginar que estamos  dizendo ao computador:
Se isso acontecer execute esta ação

Estrutura:

if (extepreção 1):
    print("A expreção 01 verdadeira")

elif (expreção 2):                      ----> Elif é um intermediário se a primeira condição não for aceita
                                        ----> execute o elif. Caso nenhuma das anteriores forem erdadeira execute
                                        ----> o else.
    print("A expreção 02 verdadeira")

else:
    print("Nenhuma das anteriores é verdadeira")

Identação

É extremamente importante se atentar à identação
'''

##Podemos também dar ao usuário a condição de inserir alguma informaçã no pronpt de comando

disciplina  = input("Entre com o nome da displina:")
semestre  = input("Entre com o sementre atual:")

if disciplina == "calculo 1" and semestre == "1":
    print("Você está periodizado!")
else:
    print("Você está desperiodizado")


#Using more the one conditional in clausele if and intruduce PLACEHOLDERS
schoolSubject = 'Data Science'
finalNote  = 90
semester = 2

if schoolSubject == "Data Science" and  finalNote >= 90 and semester != 1:
    print("Congratulations, you are aproved in %s with final averge %r!" %(schoolSubject,finalNote))
else:
    print("Sorry, but you have to stude more!")



















