import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import random
from datetime import datetime, timedelta


def dsa_gera_dados_ficticios(num_registros = 600):
    
    """
    Gera um DataFrame do Pandas de vendas ficticios
    """

    #Mensagem inicia; indicando a quantidade de registros a serem gerados
    print(f"\nIniciando a geração de {num_registros} resgistros de vendas\n")

    #Dicionário com produtos, suas categorias e preços
    produtos  = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preos':7500.00},
        'Mause Vertical': {'categoria': 'Acessório', 'preos':250.00},
        'Teclado Mecânico': {'categoria': 'Acessório', 'preos':550.00},
        'Monitor Ultawide': {'categoria': 'Eletrônicos', 'preos':2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preos':1200.00},
        'Headset 7.1': {'categoria': 'Acessório', 'preos':800.00},
        'Placa de video':{'categoria': 'Hardware', 'preos':4500.00},
        'SSD 1TB':{'categoria': 'Hardware', 'preos':600.00}
    }

    #Cria uma lista apenas com os nomes dos produtos
    lista_produtos = list(produtos.keys())
    print(f"{lista_produtos}\n")



def main():
    print("------"*10)
    print("                Stating the analyses!                    ")
    print("------"*10)
    dsa_gera_dados_ficticios()



if __name__ == '__main__':
    main()