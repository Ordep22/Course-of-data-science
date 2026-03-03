from abc import ABC, abstractmethod

from datetime import datetime

from dsautilitarios.exceptions import saldoinsuficienteError

"""
@property

Esse decorador transforma um método em uma propriedade da classe. 
Em vez de chamar obj.saldo() como se fosse uma função, você pode acessar obj.
saldo como se fosse um atributo comum. 
Isso permite controlar o acesso a atributos privados (como _saldo), aplicando lógica de 
leitura (getter) sem expor diretamente a variável interna.

@classmethod

Esse decorador 
indica que o método recebe a classe (cls) como primeiro argumento, em vez de receber a 
instância (self). 
Isso permite que o método atue no nível da classe, acessando ou  modificando  atributos  
compartilhados  por  todas  as  instâncias.  
No  exemplo,  ele  consulta  o número total de contas criadas (cls._total_contas).

@abstractmethod

Esse  decorador,  usado  junto  com  classes  abstratas  (da  biblioteca  
abc),  obriga  que qualquer subclasse da classe atual implemente esse método. 
Ele define um contrato: toda classe filha precisa fornecer a sua própria versão de sacar, 
senão não poderá ser instanciada.

"""

class Conta(ABC):

    def __init__(self, numero: int, cliente):

        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente
        self._hitorico = []
        Conta._total_contas  = +1
    
    @property
    def saldo(self):

        return self._saldo
    
    @classmethod
    def get_total_contas(cls):

        return cls._total_contas
    

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            self._hitorico.append(datetime.now(), f"DEposito de R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
    @abstractmethod
    def sacar(self, valor: float):

        """
        Método abstrato para sacas um valor. Deve ser implementado pelas subclasses.
        """
        pass

    def extrato(self):
        """
        Exibe o extrato da conta.
        """
        print(f"\n---Extrato da Conta Nº {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._saldo:2.f}")
        print("Histórico de transações:")

        if not self._hitorico:
            print("Nenhuma transação registrada.")
        
        for data, transacao in self._hitorico:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")
            print(50*"-")
            print("\n")
        



class ContaCorrente(Conta):

    def __init__(self, numero, tipo, atualizar):
        super().__init__(numero, tipo)
        self.atualizar = atualizar

class ContaPulpanca(Conta):
    pass