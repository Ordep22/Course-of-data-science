# =====================================================================
# MÓDULO PRINCIPAL DA APLICAÇÃO (main.py)
# =====================================================================

# Importa a classe Banco responsável por gerenciar clientes e contas
from dsaopoeracoes.banco import Banco

# Importa exceções personalizadas usadas no fluxo de operações
from dsautilitarios.exceptions import SaldoInsuficienteError, ContaInexistenteError


def menu_principal():
    """Exibe o menu principal e retorna a opção escolhida."""
    # REQUISITO 1: Exiba o menu principal.
    # 1. Imprima as opções: 1. Adicionar Cliente, 2. Criar Conta, 3. Acessar Conta, 4. Sair.
    # 2. Use a função input() para perguntar a opção do usuário.
    # 3. Retorne o valor digitado pelo usuário. 
    print("\n" + 30*"---" + "\n")
    print("1. Adcionar Cliente\n")
    print("2. Criar conta\n")
    print("3. Acessar conta\n")
    print("4. Sair\n")
    print("\n" + 30*"---" + "\n")
    escolha  = int(input("Escolha um opção:"))
    return escolha
    
    
def menu_conta(banco):
    """Exibe o menu de operações de uma conta específica."""
    
    # REQUISITO 2: Envolva toda a busca da conta em um bloco try/except.
    # Você precisará capturar a sua ContaInexistenteError e também ValueError (caso o usuário digite texto no lugar do número da conta).
    try:
        # REQUISITO 3: Busque a conta.
        # 1. Peça ao usuário o número da conta (lembre-se de converter o input para int!).
        # 2. Chame o método buscar_conta() do objeto 'banco' passado como parâmetro.
        numero_conta  = input("Insira o número da sua conta:")
        conta  = banco.buscar_conta(int(numero_conta))

        # REQUISITO 4: Crie o loop de operações da conta.
        # Use um 'while True' para manter o usuário neste menu até ele escolher sair.
        while True:
            # REQUISITO 5: Imprima os dados da conta e as opções.
            # Dica: Você pode acessar conta._cliente.nome e conta.saldo.
            # Opções: 1. Depositar, 2. Sacar, 3. Ver Extrato, 4. Voltar.
            # Leia a opção do usuário.
            print("\n" + 30*"---" + "\n")
            print("1. Depositar\n")
            print("2. Sacar\n")
            print("3. Ver Extrato\n")
            print("4. Valtar \n")
            print("\n" + 30*"---" + "\n")
            opcao_usuario = int(input("Entre com a opção desejada:"))

            # REQUISITO 6: Lógica de Depósito (Opção 1)
            # Peça o valor, converta para float e chame o método depositar() da conta.
            if opcao_usuario == 1:
                valor = float(input("Entre com o valor de peposito:"))
                conta.depositar(valor)
                
                
            # REQUISITO 7: Lógica de Saque (Opção 2)
            # Peça o valor, converta para float.
            # CUIDADO: Coloque a chamada conta.sacar(valor) dentro de um bloco try/except específico 
            # para capturar a exceção SaldoInsuficienteError e imprimir a mensagem de erro amigável.
            elif opcao_usuario == 2:
                try:
                    valor_saque  = float(input("Valor do saque:"))
                    conta.sacar(valor_saque)
                except:
                    SaldoInsuficienteError

            # REQUISITO 8: Lógica de Extrato (Opção 3)
            # Chame o método extrato() da conta.
            elif opcao_usuario == 3:
                conta.extrato()

            # REQUISITO 9: Lógica de Voltar (Opção 4)
            # Use o comando 'break' para quebrar este while e voltar para a função main().
            elif opcao_usuario == 4:
                break
        
            else:
                ValueError

    except ContaInexistenteError as e:
        # Imprima a mensagem de erro da exceção
        print("Conta Inexistente")
    except ValueError:
        # Imprima "Erro: Entrada inválida. Por favor, digite um número."
        print("Erro: Entrada inválida. Por favor, digite um número válido")
        


def main():
    """Função principal que controla o fluxo do sistema."""
    
    # REQUISITO 10: Inicialize o Banco.
    # Crie um objeto da classe Banco com um nome de sua escolha.
    banco  = Banco("Baco Digital DSA")
    

    # REQUISITO 11: Crie o loop infinito da aplicação.
    while True:
        # REQUISITO 12: Chame o menu_principal() e guarde a opção escolhida.
        opcao_escolhida = menu_principal()

        # REQUISITO 13: Lógica de Adicionar Cliente (Opção 1)
        # Peça o nome e o CPF (via input).
        # Chame o método adicionar_cliente() do seu banco.

        if opcao_escolhida == 1:
            nome_cliente  = input("Entre com o nome do cliente:")
            cpf_cliente  = input("Entre com seu CPF:")
            novo_cliente = banco.adicionar_cliente(nome=nome_cliente, cpf=cpf_cliente)

        # REQUISITO 14: Lógica de Criar Conta (Opção 2)
        # 1. Peça o CPF do cliente.
        # 2. Tente achar esse cliente no dicionário interno do banco (ex: banco._clientes.get(cpf)).
        # 3. Se o cliente existir, pergunte o tipo da conta e chame banco.criar_conta().
        # 4. Se não existir, imprima "Cliente não encontrado. Cadastre o cliente primeiro."
        elif opcao_escolhida == 2:
            if banco._clientes.get(cpf_cliente):
                tipo_conta = str(input("Inform o tipo de conta (Poupança ou Corrente):"))
                banco.criar_conta(cliente = novo_cliente , tipo = tipo_conta)

        # REQUISITO 15: Lógica de Acessar Conta (Opção 3)
        # Apenas chame a função menu_conta(), passando o seu objeto 'banco' como argumento.
        elif opcao_escolhida == 3:
            menu_conta(banco)

        # REQUISITO 16: Lógica de Sair (Opção 4)
        # Imprima uma mensagem de despedida e use o 'break' para encerrar o programa.
        else:
            break

# Ponto de entrada da aplicação
if __name__ == "__main__":
    main()