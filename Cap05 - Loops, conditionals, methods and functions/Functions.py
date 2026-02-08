# Função também são conhecidas como subrotinas

'''
Função é um dispositivo que agurpa um conjunto de instruções para
quel elas possam ser executadas mais de uma vez. Funções também permitem
especificar os parâmetros que podem servri como entrada para as funções

Em um nível mais fundamental, a cinstrução de funcões nos permite reutilizar códigos,
 sem a necessidade de reescrevê-los novamente. Com funç˜˜es, escrevemos o código uma vez
 e repetimos a mesma instrução, chamando a função, quantas vezes forem necessárias.

 Estrutura de uma função:


 def nome da função (arg01, arg02):
    "Aqui pode entrar um comentário sobre o funcionamento da função"
    <instruções a serem  executadas>
    <retorno das funções executadas>
'''

'''

Uma boa prática no uso das funções é escrever os nomes da seguintes forma

primeraPalavar  => A primeira letra da primeira palavra será minusculo 
                          => A primeira letra da segunda palavra será maiúscula 

***Isso não é uma regra mas sim uma recomendação de boas práticas


'''


def printConsole():
    print("Ola mundo!")


##Variáveis locais e variávsi globais

var_global = 10


def produto(x, y):
    var_local = x * y
    return print(var_local)


produto(var_global, 2)

'''
É interessante nomearmos as funções com u nome que as descreva 
e seja de fácil entendimento para que elas servem
'''

'''
Podem haver casos em que são sabemos quantos parâmetro serão passados
para um função, assim, podemo usar a seguinte ferramenta de passar um conjunto de informações
'''



''''
Whem you define the function's paramter with "*parameter". 
It means witch you can pass or not and the function will run normaly
'''
# def printaVarinfo(arg1, *vartuple):
#     print("O parâmetro passado foi:", arg1)
#
#     for i in vartuple:
#         print("O parâmetro passado foi:", i)
#
#
# printaVarinfo("Mamão", "Abacate", "Laraja")

"""
Expressões Lambda 
    
    Uma da caracteristicas mais úteis em python é a expressão lambda. Expressões 
    lambda permitem criar funções "Anônimas". Isto significa que podemos 
    fazer rapidamente funções ad-hoc sem a necessidade de definir uma função usando a palavra def


    Objetos de funções desenvolvidos executando expressões lambda 
    funcionam exatamente da mesma forma como aqueles criados e atribuidos pela palavra reservada def.
    Mas há algumas diferenças:
    
     - O corpo da lambda é uma única expressão, não um bloco de instruções
     - O corpo do lambda é semelhante a uma instrução de retorno do corpo def
     
    Expressões lambda rea;mente são úteis, quando usads em conjunto com as funções map(), filter(), reduce()
    
    Expressões lambda podem ser usadas para criar funcões simples. Também chamdas de funcões in-line ou apenas funções anônimas
    
    lambda 2:2**2
     
     Deferenças entre def e lambda para criar funçcões
     
     def => Cria um objeto e atribui um nome a ele (nome da função)
     lambda => Cria um objeto, mas o retorna como resultado em tempo de execução
     


potencia = lambda num: num ** 2

print(potencia(2))

#Global VAR
varGlobal  = 10
print(varGlobal)


#Function
def function(num1,num2):
    varGlobal = num1 +num2
    print(varGlobal)

function(1,2)


Out put - 
10 - global 
3 - local 
Is clear witch the global variable it inst the same local variable


"""
#Finish the lesson Functions

#This function split the string by its spaces
def SplitStringWords(text):
    return text.split(" ")

text = " This function will be useful to split bisg values of datas"

#Split text implementing the new function
print(SplitStringWords(text))




#Function arguments with default values

def test_function(number_of_itens, item_name  = "Tenis"):
    print(f"Você tem {number_of_itens} {item_name}")

test_function(10)
test_function(10, "Camisetas")

    

#Functions with variable number of arguments
""""
The *args and **kwargs are used in function definitions to allow for a variable number of arguments to be passed to the function.
"""
def sum_all(*args):
    sum  = 0
    for i in args:
        sum += i
    return sum

print(sum_all(1,2,3,4,5))
print("\n\n-----------------------------\n\n")

def exibe_all_people(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

exibe_all_people(name="John", age=30, city="New York", occupation="Developer")

print("\n\n-----------------------------\n\n")


    
#Lambda functions

my_data_list = [1, 2, 3, 4, 5]

#Using lambda function to square each element in the list
my_new_list = list(map(lambda x: x ** 2,my_data_list))
print(my_new_list)


my_new_par_lis = list(filter(lambda x:x % 2 == 0, my_new_list))
print(my_new_par_lis)


a = "Pedro"

upper = lambda x:x.upper()

print(upper(a))












