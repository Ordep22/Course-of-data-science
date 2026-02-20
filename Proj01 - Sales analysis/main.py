import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random
from datetime import datetime, timedelta
import os
from matplotlib.ticker import FuncFormatter



def dsa_gera_dados_ficticios(num_registros: int = 10000) -> pd.DataFrame:

    """
    Gera um dataFrame do Pandas com dados de vendas fictícios.
    """
    #Mensagem inicial indicando a quantidade de registros serão gerados
    print(f"\nIniciando a geração de {num_registros} registros de vendas ...")

    #Dicionário com produtos, suas categorias e preços
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }

    #Cria uma lista apensad com os nomes dos produtos
    lista_produtos  = list(produtos.keys())

    #Dicionário com cidades e seus respectivos estados
    cidades_estado = {"São Paulo":"SP", "Rio de Janeiro":"RJ", "Belo Horizonte":"MG", 
                      "Curitiba":"PR", "Porto Alegre":"RS", 'Fortaleza': 'CE', "Salvador": "BA"}
    
    #Cra uma lista apenas com os nomes das cidades
    lista_cidades = list(cidades_estado.keys())

    #Lista que armazena os registros de vendas
    dados_vendas  = []

    #Define a data inicial dos pedidos
    data_inicial  = datetime(2025, 1, 1)

    data_final = datetime(2026,2,20)

    

    #Loop para gerar os registros de vendas
    for i in range(num_registros):

        #Seleciona um produto aleatório
        produto_nome = random.choice(lista_produtos)

        #Seleciona aleatoriamente a cidade de venda
        cidade = random.choice(lista_cidades)

        #Gegra uma quantidade de produtos vendida entre 1 e 7
        quantidade = random.randint(1, 8)

        #Calcula a data do pedido a partir da data inicial
        data_pedido  = data_inicial + timedelta(days = random.randint(0,365), hours = random.randint(0, 23)) 

        #Se o produto for Muse ou Teclado, aplica desconto aleatório entre 5% e 15%

        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            produto_unitario = produtos[produto_nome]['preco'] * (1 - random.uniform(0.05, 0.15))
        else:
            produto_unitario = produtos[produto_nome]['preco']
        
        #Adciona um registro de venrda à Lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data do Pedido': data_pedido,
            'Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preço Unitário': round(produto_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estado[cidade],
            
        })

    #Mensagem final incicando que a geração terminou
    print(f"\nGeração de dados concluída! {num_registros} registros de vendas foram gerados com sucesso.")

    #Retorn os dado no formato de DataFrame do Pandas
    return pd.DataFrame(dados_vendas)






def main():

    #Gerando, carregando e explorando os dados

    #Gerar dados de venda fictícios
    df_vendas = dsa_gera_dados_ficticios(10000)

    #Mostra o início do DataFrame gerado
    print(f"\nOs dados de venda são:")
    print(df_vendas.head(5))
    print('\n')

    #Mostra o final do DataFrame gerado
    print(df_vendas.tail())

    #Mostra o typo do DataFrame gerado
    print(df_vendas.dtypes)

    #Mostra o shape do DataFrame gerado
    print(df_vendas.shape)

    #Exibe informações gerais sobre o DataFrame (tipos de dados, valores não nulos)
    print(df_vendas.info())

    #Exibe o resumo estatístico do DataFrame (média, desvio padrão, valores mínimos e máximos)
    print(df_vendas.describe())


    #Limpeza, Pré-processamento e Engenharia de atributos

    # Se a coluna 'Data_Pedido' não estiver como tipo datetime, precisamos fazer a conversão explícita
    # A coluna pode ser usada para análise temporal
    print(f"\nVerificando o tipo dos dados de 'Data do Pedido': {df_vendas['Data do Pedido'].dtype}")
    df_vendas['Data do Pedido'] = pd.to_datetime(df_vendas['Data do Pedido'])
    print(f"\nVerificando o tipo dos dados de 'Data do Pedido' após conversão: {df_vendas['Data do Pedido'].dtype}")

    # Engenharia de atributos
    # Criando a coluna 'Faturamento' (preço x quantidade)   
    df_vendas['Faturamento'] = df_vendas['Preço Unitário'] * df_vendas['Quantidade']
    print(f"\nVerificando os primeiros valores da coluna 'Faturamento':\n{df_vendas['Faturamento'].head()}")

    # Engenharia de atributos
    # Usando uma função lambda para criar uma coluna de status de entrega
    df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: 'Rápida' if estado in ['SP', 'RJ', 'MG'] else 'Normal')

    #Exibe informações gerais sobre o DataFrame (tipo de dados, valores não nulos)
    df_vendas.info()


    #Análise 1 - Top 10 produtos mais vendidos
    print("\nAnálise 1 - Top 10 produtos mais vendidos")
    top_10_produtos  = df_vendas.groupby('Produto')['Quantidade'].sum().sort_values(ascending = False).head(10)
    print(f"\nTop 10 produtos mais vendidos:\n{top_10_produtos}")


    #Mostrando o gráfico de barras dos top 10 produtos mais vendidos
    
    #Define um estilo para os gráficos
    sns.set_style('whitegrid')

    #Cria a figura e os exios
    plt.figure(figsize=(12, 7))

    #Cria o gráfico de barras horizontal
    top_10_produtos.sort_values(ascending=True).plot(kind='barh', color='red', edgecolor='black')

    #Adciona títulos e lables
    plt.title('Top 10 Produtos Mais Vendidos', fontsize=16)
    plt.xlabel('Quantidade Vendida', fontsize=12)
    plt.ylabel('Produto', fontsize=12)

    #Exibe o gráfico
    plt.tight_layout()
    plt.show()


    #Análise 2  - Faturamento Mensal
    print("\nAnálise 2 - Faturamento Mensal")
    print(df_vendas.head())
    df_vendas['Mes'] = df_vendas['Data do Pedido'].dt.to_period('M')
    print(df_vendas.head())

    #Agrupando por mêse somando o faturmaneot
    faturamento_mensal  = df_vendas.groupby('Mes')['Faturamento'].sum()

    #Converte o índice para string para facilitar aplotagem no gráfico
    faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')

    faturamento_mensal.map('R$ {:,.2f}'.format)
    print(f"\nFaturamento mensal:\n{faturamento_mensal}")
    

    #Cria uma nova figura com tamanho de 12 por 6 polegadas
    plt.figure(figsize = (12,6))
    faturamento_mensal.plot(kind = 'line', marker = 'o', linestyle = '-', color = 'green')
    plt.title('Faturamento Mensal', fontsize=16)
    plt.xlabel('Mês', fontsize=12)
    plt.ylabel('Faturamento (R$)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True,which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()


    #Analise 3  - Vendas por Estado
    vendas_por_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending=False)
    
    #Formata para duas casa decimais
    vendas_por_estado.map('R$ {:,.2f}'.format)

    # Cria uma nova figura com tamanho de 12 por 7 polegadas
    plt.figure(figsize = (12, 7))

    # Plota os dados de faturamento por estado em formato de gráfico de barras
    # Usando a paleta de cores "rocket" do Seaborn
    vendas_por_estado.plot(kind = 'bar', color = sns.color_palette("husl", 7))

    # Define o título do gráfico com fonte de tamanho 16
    plt.title('Faturamento Por Estado', fontsize = 16)

    # Define o rótulo do eixo X
    plt.xlabel('Estado', fontsize = 12)

    # Define o rótulo do eixo Y
    plt.ylabel('Faturamento (R$)', fontsize = 12)

    # Mantém os rótulos do eixo X na horizontal (sem rotação)
    plt.xticks(rotation = 0)

    # Ajusta automaticamente os elementos do gráfico para evitar sobreposição
    plt.tight_layout()

    # Exibe o gráfico
    plt.show()


    #Análise 4 - Faturmanto por Categoria

    #Agrupa por categoria, soma o faturmento e formara como meda para melhorar leitura
    faturamento_categoria  = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)

    #Formata para melhor visualisação
    faturamento_categoria.map('R$ {:,.2f}'.format)

    print(f"\n\n O faturamento por categoria é: \n{faturamento_categoria}")


    #Ordena os dados para o gráfico ficar mais fácil de ler
    faturamento_ordenado = faturamento_categoria.sort_values(ascending=False)

    #Cria a Figura e o Eixos (ax) com plt.subplots()
    #Isso nos dá mais controle sobre os elementos gráfcos.
    fig, ax = plt.subplots(figsize = (12,7))

    #Cria uma função para formatar os números
    #Esta função recebe um valor 'y' e o transforma em uma string no formato 'R$ XX K'
    def formatador_milhares(y,pos):
        """Formata o valor em milhares (K) cm cifrão R$."""
        return f'R$ {y/1000:,.0f}K'

    # Cria o objeto formatador
    formatter = FuncFormatter(formatador_milhares)

    # Aplica o formatador ao eixo Y (ax.yaxis)
    ax.yaxis.set_major_formatter(formatter)

    # Plota os dados usando o objeto 'ax'
    faturamento_ordenado.plot(kind = 'bar', ax = ax, color = sns.color_palette("viridis", len(faturamento_ordenado)))


    #Adiciona títulos e labels usando 'ax.set_..'
    ax.set_title('Faturamento Por Categoria', fontsize = 16)
    ax.set_xlabel('Categoria', fontsize = 12)
    ax.set_ylabel('Faturamento', fontsize = 12)

    #Ajusta a rotação dos rótulos do eixo x
    plt.xticks(rotation = 45, ha = 'right')

    #Garante que tudo fique bem ajustado na imagem final
    plt.tight_layout()

    # Exibe o gráfico
    plt.show()
    





if __name__ == '__main__':
    main()
