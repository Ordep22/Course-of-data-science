# Importa a classe base abstrata e o decorador para métodos abstratos
from abc import ABC, abstractmethod

# Importa a classe datetime para registrar data e hora das transações
from datetime import datetime

# Simulação da importação da exceção (como se estivesse no seu arquivo dsautilitarios)
#from dsautilitarios.exceptions import SaldoInsuficienteError
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_disponivel, valor, mensagem="Saldo insuficiente."):
        super().__init__(f"{mensagem} Saldo/Limite disponível: R${saldo_disponivel:.2f}, Valor tentado: R${valor:.2f}")

# =====================================================================
# CLASSE BASE: CONTA (ABSTRATA)
# =====================================================================
class Conta(ABC):
    """
    Classe base abstrata para contas bancárias.
    Demonstra Herança e Encapsulamento.
    """
    _total_contas = 0

    def __init__(self, numero: int, cliente):
        # REQUISITO 1: Inicialize os atributos da conta.
        # Defina o número da conta (protegido).
        self._numero = numero
        # Defina o saldo da conta, inicializado em 0.0 (protegido).
        self._saldo  = 0.0
        # Defina a referência ao cliente dono da conta (protegido).
        self._cliente  = cliente
        # Inicialize a lista _historico como uma lista vazia (protegido).
        self._historico  = []


        # REQUISITO 2: Incremente o atributo de classe _total_contas.
        Conta._total_contas += 1 
  

    @property
    def saldo(self):
        """Getter para o saldo, permitindo acesso controlado."""
        # REQUISITO 3: Retorne o valor do saldo protegido.
        return self._saldo
    

    @classmethod
    def get_total_contas(cls):
        """Método de classe para obter o número total de contas criadas."""
        # REQUISITO 4: Retorne a variável de classe que armazena o total de contas.
        return cls._total_contas

    def depositar(self, valor: float):
        """Adiciona um valor ao saldo da conta."""
        # REQUISITO 5: Implemente a lógica de depósito.
        # Verifique se o valor é maior que 0. Se não for, imprima "Valor de depósito inválido."
        # Se for válido:
        # 1. Incremente o saldo.
        # 2. Adicione uma tupla ao _historico contendo a data atual (datetime.now()) e a mensagem "Depósito de R$XX.XX".
        # 3. Imprima uma mensagem de sucesso.
        if valor > 0:
            self._saldo += valor
            self._historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido!")

    """
    Quando se usa o decorador @abstractmethod isso informa ao Python que 
    o método será implmentado pelas classe filho.
    """
    @abstractmethod
    def sacar(self, valor: float):
        """Método abstrato para sacar um valor. Deve ser implementado pelas subclasses."""
        pass

    def extrato(self):
        """Exibe o extrato da conta."""
        # A implementação do extrato já está fornecida para você testar depois
        print(f"\n--- Extrato da Conta Nº {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._saldo:.2f}")
        print("Histórico de transações:")

        if not self._historico:
            print("Nenhuma transação registrada.")

        for data, transacao in self._historico:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")
        print("--------------------------------------\n")


# =====================================================================
# EXERCÍCIO 1: CONTA CORRENTE
# =====================================================================
class ContaCorrente(Conta): # Herança já definida
    """
    Subclasse que representa uma conta corrente.
    Demonstra Polimorfismo ao sobrescrever o método sacar com limite (cheque especial).
    """

    def __init__(self, numero: int, cliente, limite: float = 500.0):
        # REQUISITO 6: Chame o construtor da classe base (Conta) passando 'numero' e 'cliente'.
        super().__init__(numero,cliente)
        
        # REQUISITO 7: Inicialize o atributo 'limite'.
        self.limite  = limite
        pass

    def sacar(self, valor: float):

        """Permite saque utilizando o saldo da conta mais o limite (cheque especial)."""
        # REQUISITO 8: Implemente a lógica de saque para Conta Corrente.
        # 1. Verifique se o valor é menor ou igual a 0. Se sim, imprima erro e retorne.
        # 2. Calcule o 'saldo_disponivel' (saldo atual + limite). Lembre-se de acessar o saldo como um atributo protegido da classe pai.
        # 3. Se o valor de saque for maior que o saldo_disponivel, levante (raise) um SaldoInsuficienteError.
        # 4. Caso contrário, deduza o valor do saldo.
        # 5. Adicione a transação ao _historico (similar ao depósito).
        # 6. Imprima mensagem de sucesso.
        if valor > 0:
            saldo_disponivel  = self._saldo + self.limite

            if valor <= saldo_disponivel:

                self._saldo -= valor
                self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            
            else:
                raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficientes.")

        else:
            print(f"O valor {valor:.2f} é um valor inválido!")     


# =====================================================================
# EXERCÍCIO 2: CONTA POUPANÇA
# =====================================================================
class ContaPoupanca(Conta): # Herança já definida
    """Subclasse que representa uma conta poupança (saque apenas com saldo positivo)."""

    def __init__(self, numero: int, cliente):
        # REQUISITO 9: Chame o construtor da classe base.
        super().__init__(numero,cliente)

    def sacar(self, valor: float):
        """Implementação do método sacar apenas com saldo disponível."""
        # REQUISITO 10: Implemente a lógica de saque para Conta Poupança.
        # 1. Verifique se o valor é menor ou igual a 0. Se sim, imprima erro e retorne.
        # 2. Verifique se o valor é maior que o saldo atual.
        # 3. Se for maior, levante (raise) um SaldoInsuficienteError.
        # 4. Caso contrário, deduza o valor do saldo.
        # 5. Adicione a transação ao _historico.
        # 6. Imprima mensagem de sucesso.
        if valor > 0: 

            if valor <= self._saldo:

                self.saldo -= valor
                self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            
            else:
                raise SaldoInsuficienteError(self._saldo, valor, "Saldo insuficientes.")

        else:
            print(f"O valor {valor:.2f} é um valor inválido!")     


