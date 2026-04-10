# =====================================================================
# MÓDULO DE EXCEÇÕES CUSTOMIZADAS
# =====================================================================

# REQUISITO 1: Faça a classe SaldoInsuficienteError herdar da classe base 'Exception'
class SaldoInsuficienteError(Exception):
    """Exceção levantada quando uma operação de saque excede o saldo disponível."""

    def __init__(self, saldo_atual, valor_saque, mensagem="Saldo insuficiente para realizar o saque."):
        
        # REQUISITO 2: Salve o 'saldo_atual' recebido como um atributo da instância.
        self.saldo_atual  = saldo_atual
        
        # REQUISITO 3: Salve o 'valor_saque' recebido como um atributo da instância.
        self.valor_saque  = valor_saque
        
        # REQUISITO 4: Crie uma mensagem formatada.
        # Junte a 'mensagem' padrão com os valores de saldo_atual e valor_saque.
        # Dica: Use f-strings e formate os valores para duas casas decimais (ex: R$10.50).
        # Salve essa string montada em um atributo chamado 'self.mensagem'.
        self.mensagem  = f"{mensagem} O saldo atual é: {self.saldo_atual}. A tentativa de saque foi: {self.valor_saque}"
        
        # REQUISITO 5: Inicialize a exceção base.
        # Chame o construtor da superclasse (Exception) passando a 'self.mensagem' que você acabou de criar.
        super().__init__(self.mensagem)


# REQUISITO 6: Faça a classe ContaInexistenteError herdar da classe base 'Exception'
class ContaInexistenteError(Exception):
    """Exceção levantada ao tentar operar em uma conta que não existe."""
    
    def __init__(self, numero_conta, mensagem="A conta especificada não foi encontrada."):
        
        # REQUISITO 7: Salve o 'numero_conta' recebido como um atributo da instância.
        self.numero_conta  = numero_conta
        
        
        # REQUISITO 8: Crie uma mensagem formatada.
        # Junte a 'mensagem' padrão indicando qual foi o 'numero_conta' que gerou o erro.
        # Salve essa string em 'self.mensagem'.
        self.mensagem  = f"{mensagem} Numero da conta: {self.numero_conta}"
        
        
        # REQUISITO 9: Inicialize a exceção base.
        # Chame o construtor da superclasse (Exception) passando a sua 'self.mensagem'.
        super().__init__(self.mensagem)
        