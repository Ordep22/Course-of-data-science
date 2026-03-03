#Class Cliente - Cria a gerencia a classe clientes

class Cliente:

    def __init__(self, nome: str, cpf: int) -> None:
        
        self.nome = nome
        self.cpf = cpf
        self.conta = []
    
    def adciona_conta(self, conta):

        self.conta.append(conta)
    
    def __str__(self):
    
        return f"Cliente: {self.nome} (CPF: {self.cpf})"