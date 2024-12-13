import os
import time
import titulo
import app
import pandas as pd
from app import *
from sqlalchemy import create_engine, MetaData, Table, inspect

def buscar():
    print('Buscar')
    time.sleep(1)
    os.system('cls')
    titulo.titulo()
    opcoes_buscar()
    escolhas_buscar()

def opcoes_buscar():
    print("Buscar por: \n", '|1 - Nome|', '|2 - Tipo|', '|3 - Número|\n', '|4 - Menu|', '|5 - Sair|')
    

def escolhas_buscar():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                busca_por_nome()
            case 2:
                busca_por_tipo()
            case 3:
                busca_por_numero()
            case 4:
                voltar_ao_menu()
            case 5:
                finalizar_app()
            case _:
                buscar()
    except ValueError:
        buscar()

def busca_por_nome():
    print("busca por nome")
    entrada = input("Digite o nome do pokemon: ")
    nome = entrada.title()
    engine = create_engine('sqlite:///:memory:')
    app.df.to_sql('pkm', engine)
    query = f"SELECT * FROM pkm WHERE Name='{nome}'"
    df_nome = pd.read_sql(query, engine)
    
    os.system('cls')
    titulo.titulo()
    print('\n')
    print(df_nome,'\n')
    opcoes_buscar()
    escolhas_buscar()
    
def busca_por_tipo():
    print("busca por tipo")
    time.sleep(1)
    buscar()

def busca_por_numero():
    print("busca por numero")
    time.sleep(1)
    buscar()


def voltar_ao_menu():
    ''' Retorna ao menu'''
    print('\nVoltando ao menu. ')
    time.sleep(1)
    os.system('cls')
    titulo.titulo()
    app.exibir_opcoes()
    app.escolher_opcao()

def exibir_subtitulo(texto):
    '''Exibe uma linha de texto como subtitulo em destaque refente a opção escolhida.
    
    Input:
    - texto: str - o texto do subtitulo'''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    '''Encerra o app limpando a tela apoz uma mensagem de emcerramento'''

    exibir_subtitulo('Obrigado por testar! (◍ ˃̵͈̑ᴗ˂̵͈̑)')