import modulosdsa

mensagem  = modulosdsa.dsa_saudacao("Mundo")
print(mensagem)
print(f"O valor de PI do nosso módulo é: {modulosdsa.PI}")

from modulosdsa import dsa_saudacao, PI

mensagem_direta  = dsa_saudacao("Aluno DSA")
print(mensagem_direta)
print(f"O valor de PI importado diretamente: {PI}")
