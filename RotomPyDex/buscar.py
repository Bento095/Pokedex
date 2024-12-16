import os
import time
import titulo
import main as main
import pandas as pd

from main import *
from sqlalchemy import create_engine, MetaData, Table, inspect
from explorar import *


def buscar(): # responsavel pela estrutura da função
    print('Buscar')
    time.sleep(1)
    os.system('cls')
    titulo.titulo()
    opcoes_buscar()
    escolhas_buscar()

def opcoes_buscar(): # exibido para auxiliar a navegação
    print("Buscar por: \n", '|1 - Nome|', '|2 - Tipo|', '|3 - Número|\n', '|4 - Menu|', '|5 - Sair|')
    

def escolhas_buscar(): #bloco principal da navegação, recebe o imput e executa o bloco respectivo
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

def busca_por_nome(): #funçâo vai receber um texto do usuario, tratar para inicial maiuscula como no padrão doa dados e fazer uma busca criando um novo df, depois verificando se o texto inserido faz parte na coluna Name, caso contrario o bloco reinicia
    try:
        print("busca por nome")
        entrada = input("Digite o nome do pokemon: ")
        nome = entrada.title()
        engine = create_engine('sqlite:///:memory:')
        main.df.to_sql('pkm', engine)
        query = f"SELECT * FROM pkm WHERE Name='{nome}'"
        df_nome = pd.read_sql(query, engine)
        if nome not in df_nome['Name'].values:
            print("Pokémon não encontrado, tente de novo.")
            time.sleep(1)
            busca_por_nome()
        else: #caso o texto seja o nome de um pokemon o novo dataframe é exibido ao usuario com o estilo do app, voltando a apresentar opcões de navegação
            os.system('cls')
            titulo.titulo()
            print('\n')
            print(df_nome,'\n')
            opcoes_buscar()
            escolhas_buscar()
    except ValueError:
        busca_por_nome
    
def busca_por_tipo(): # este foi chatinho e devera receber mais atenção guando o progeto receber uma GUI, deixando a navegação entre as paginas viaveis.
    print("busca por tipo")
    entrada = input("Digite o tipo do pokemon: ")
    tipo = entrada.lower()
    engine = create_engine('sqlite:///:memory:')
    main.df.to_sql('pkm', engine)
    query = f"SELECT * FROM pkm WHERE \"Type 1\" = '{tipo}' OR \"Type 2\" = '{tipo}'"
    df = pd.read_sql(query, engine) 
    print(df)
    opcoes_buscar()
    escolhas_buscar()

def busca_por_numero():#aqui o codigo é bem parecido com o de busca_por_nome, mas tive erros por passar a coluna No. sem os colchetes, o tratamento com a entrada tbm so converte para inteiro ja que é esperado apenas nùmeros
    try:
        print("busca por número")
        numero = int(input("Digite o número do pokemon: "))
        engine = create_engine('sqlite:///:memory:')
        main.df.to_sql('pkm', engine)
        query = f"SELECT * FROM pkm WHERE [No.]='{numero}'"
        df_numero = pd.read_sql(query, engine)
        print(df_numero)
        if numero not in df_numero['No.'].values:
            print("Pokémon não encontrado, tente de novo.")
            time.sleep(1)
            busca_por_numero()
        else:
            os.system('cls')
            titulo.titulo()
            print('\n')
            print(df_numero,'\n')
            opcoes_buscar()
            escolhas_buscar()
    except ValueError:
        busca_por_numero()

def voltar_ao_menu(): # deve ir para um app separado no futuro
    ''' Retorna ao menu'''
    print('\nVoltando ao menu. ')
    time.sleep(1)
    os.system('cls')
    titulo.titulo()
    main.exibir_opcoes()
    main.escolher_opcao()

def exibir_subtitulo(texto):# deve ir para um app separado no futuro
    '''Exibe uma linha de texto como subtitulo em destaque refente a opção escolhida.
    
    Input:
    - texto: str - o texto do subtitulo'''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():# deve ir para um app separado no futuro
    '''Encerra o app limpando a tela apoz uma mensagem de emcerramento'''

    exibir_subtitulo('Obrigado por testar! (◍ ˃̵͈̑ᴗ˂̵͈̑)')