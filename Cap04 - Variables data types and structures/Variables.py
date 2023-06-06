"""
Variável é o nome utilizado para definir um ou mais valores que são
manipulados pelos programas durante a sua operação.
O nome “variável” é utilizado por ser um tipo de conteúdo que pode
apresentar diferentes valores enquanto o sistema está em execução.
"""
"""
A lingugem python tem tipificação dinâmica. Isso significaca que o interpretador 
Python identifica automaticamente qual o tipo da variável declarada.

"""

meuNumero  = 18
tipo  = type(meuNumero)


print(f"O tipo do meu número é: {type(meuNumero)}")

"""
Em Pyhton é possível declarar multipla variáveis em uma única linha


"""

#Cada variável recebe seu valor individualmente

pessoa1, pessoa2, pessoa3 = "Pedro", "Vitor ", "Pereira"

print(f"O nome da pessoa um é: {pessoa1}")

print(f"O nome da pessoa um é: {pessoa2}")

print(f"O nome da pessoa um é: {pessoa3}")

#As variáveis recebem os mesmo valores

fruta1 = fruta2 = fruta3 = "Melancia"

print(f"A fruta  é: {fruta1}")



"""
Existem alguma regras na liguamgem Python quanto a declaração de 
variáveis. 
Uma dos nomes que são proibidos é a declaração com nomes de reservados
"""

#É possível utlizar letras e número nos nomes das variávie mas eles devem
#respeitar uma sequência.

#O nome da variável pode finalizar com um número mas não pode inciar com um

x1 = 10
print(f"O valor de x1 é: {x1}")

#Essa notação está incorreta seu código não iria ser compilado
#1x  = 11


"""
Concatenação de variáveis

Em python o operador + quand utilizado para somar duas variáveis do 
tipo string realiza a concatenação

"""

nome  = "Bob"

sobrenome  = "Marley"

nomeCompleto  = nome + " " + sobrenome

print(f"O nome completo é: {nomeCompleto}")














