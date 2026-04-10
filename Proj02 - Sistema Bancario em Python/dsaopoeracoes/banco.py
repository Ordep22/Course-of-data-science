# Importa a classe Cliente (assumindo que você já tem ou fará esse arquivo)
from dsaentidades.cliente import Cliente

# Importa a classe base Conta e suas subclasses
from dsaentidades.conta import Conta, Conta_Corrente, Conta_Poupanca

DEBUG = True

# Importa exceção personalizada
# from dsautilitarios.exceptions import ContaInexistenteError
class ContaInexistenteError(Exception):
    def __init__(self, numero_conta):
        super().__init__(f"Erro: A conta número {numero_conta} não existe no sistema.")

# =====================================================================
# CLASSE GERENCIADORA: BANCO
# =====================================================================
class Banco:
    """
    Classe que gerencia as operações do banco.
    Demonstra Composição, pois "tem" clientes e contas.
    """

    def __init__(self, nome: str):
        # REQUISITO 1: Inicialize os atributos do banco.
        # 1. Salve o 'nome' recebido no parâmetro em um atributo da instância.
        # 2. Crie um atributo protegido '_clientes' inicializado como um dicionário vazio (vai guardar CPF -> Objeto Cliente).
        # 3. Crie um atributo protegido '_contas' inicializado como um dicionário vazio (vai guardar Numero -> Objeto Conta).
        self.nome = nome
        self._clientes  = {}
        self._contas = {}

    def adicionar_cliente(self, nome: str, cpf: str) -> Cliente:
        """Cria e adiciona um novo cliente ao banco."""
        
        # REQUISITO 2: Verifique se o cliente já existe.
        # Verifique se o 'cpf' passado já é uma chave no dicionário self._clientes.
        # Se for, imprima uma mensagem de erro e retorne o cliente existente.
        if cpf in self._clientes:
            print(f"ERRO: O cliente {nome} já está cadastrado!")
            return self._clientes[cpf]
        
        # REQUISITO 3: Crie e cadastre o novo cliente.
        # 1. Instancie um novo objeto da classe Cliente passando o nome e cpf.
        # 2. Adicione esse novo objeto ao dicionário self._clientes, usando o cpf como chave.
        # 3. Imprima uma mensagem de sucesso ("Cliente X adicionado com sucesso").
        # 4. Retorne o objeto cliente recém-criado.

        novo_cliente = Cliente(nome, cpf)
        self._clientes[cpf] = novo_cliente

        print(f"Cliente {nome} adicionado com sucesso")
        return novo_cliente

    def criar_conta(self, cliente: Cliente, tipo: str) -> Conta:
        """Cria uma nova conta para um cliente existente."""
        
        # REQUISITO 4: Defina o número da nova conta.
        # Use o método de classe 'get_total_contas()' da classe Conta, e some 1 para gerar o novo número.
        numero_conta  = Conta.get_total_contas() + 1 
        
        # REQUISITO 5: Instancie a conta correta baseada no parâmetro 'tipo'.
        # DICA: Use tipo.lower() para evitar problemas com letras maiúsculas/minúsculas.
        # 1. Se o tipo for 'corrente', crie um objeto ContaCorrente.
        # 2. Se o tipo for 'poupanca', crie um objeto ContaPoupanca.
        # 3. Se não for nenhum dos dois, imprima uma mensagem de erro ("Tipo inválido") e retorne None.

        if DEBUG:
            print("\nDEBUG Mode: Active")
            print("Testanto a construção do novo objeto")
            print(f"Nome do clienete: {cliente.nome}")
            print(f"CPF: {cliente.cpf}")
            print(f"Tipo de conta: {tipo}\n")


        if tipo.lower() == "corrente":
             
            nova_conta  = Conta_Corrente(numero_conta, cliente)

        elif tipo.lower() == "poupança":

            nova_conta  = Conta_Poupanca(numero_conta, cliente)

        else:
            print("Tipo inválido!!!")
            return None


        # REQUISITO 6: Registre a conta no banco e no cliente.
        # 1. Adicione a nova conta ao dicionário self._contas, usando o numero_conta como chave.
        # 2. Chame o método 'adicionar_conta()' do objeto 'cliente' passando a nova conta (isso faz a associação bidirecional).
        # 3. Imprima uma mensagem de sucesso ("Conta criada...").
        # 4. Retorne o objeto da nova conta.
        self._contas[numero_conta] = nova_conta 
        cliente.adiciona_conta(nova_conta)
        print(f"Conta {tipo} nº {numero_conta} criada para o cliente {cliente.nome}.")
        return nova_conta

    def buscar_conta(self, numero_conta: int) -> Conta:
        """Busca uma conta pelo seu número."""
        
        # REQUISITO 7: Busque a conta e trate o caso de não existir.
        # 1. Tente pegar a conta no dicionário self._contas usando o numero_conta. (Dica: o método .get() de dicionários é ótimo aqui).
        # 2. Se a conta não for encontrada (for None/False), levante (raise) a exceção ContaInexistenteError.
        # 3. Se encontrar, retorne o objeto conta.
        conta  = self._contas.get(numero_conta)
        if conta:
            return conta
        else:
            raise ContaInexistenteError(numero_conta)