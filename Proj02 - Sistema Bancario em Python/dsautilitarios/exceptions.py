# =====================================================================
# MÓDULO DE EXCEÇÕES CUSTOMIZADAS
# =====================================================================

# REQUISITO 1: Faça a classe SaldoInsuficienteError herdar da classe base 'Exception'
class SaldoInsuficienteError( ... ):
    """Exceção levantada quando uma operação de saque excede o saldo disponível."""

    def __init__(self, saldo_atual, valor_saque, mensagem="Saldo insuficiente para realizar o saque."):
        
        # REQUISITO 2: Salve o 'saldo_atual' recebido como um atributo da instância.
        pass
        
        # REQUISITO 3: Salve o 'valor_saque' recebido como um atributo da instância.
        pass
        
        # REQUISITO 4: Crie uma mensagem formatada.
        # Junte a 'mensagem' padrão com os valores de saldo_atual e valor_saque.
        # Dica: Use f-strings e formate os valores para duas casas decimais (ex: R$10.50).
        # Salve essa string montada em um atributo chamado 'self.mensagem'.
        pass
        
        # REQUISITO 5: Inicialize a exceção base.
        # Chame o construtor da superclasse (Exception) passando a 'self.mensagem' que você acabou de criar.
        pass


# REQUISITO 6: Faça a classe ContaInexistenteError herdar da classe base 'Exception'
class ContaInexistenteError( ... ):
    """Exceção levantada ao tentar operar em uma conta que não existe."""
    
    def __init__(self, numero_conta, mensagem="A conta especificada não foi encontrada."):
        
        # REQUISITO 7: Salve o 'numero_conta' recebido como um atributo da instância.
        pass
        
        # REQUISITO 8: Crie uma mensagem formatada.
        # Junte a 'mensagem' padrão indicando qual foi o 'numero_conta' que gerou o erro.
        # Salve essa string em 'self.mensagem'.
        pass
        
        # REQUISITO 9: Inicialize a exceção base.
        # Chame o construtor da superclasse (Exception) passando a sua 'self.mensagem'.
        pass