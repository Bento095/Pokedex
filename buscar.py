import os
import time
import titulo
import app

from app import *

def buscar():
    os.system('cls')
    print('Buscar')
    opcoes_buscar()
    escolhas_buscar()

def opcoes_buscar():
    titulo.titulo()
    print("Buscar por: \n", '|1 - Nome|', '|2 - Tipo|', '|3 - Número|\n', '|4 - Menu|', '|5 - Sair|')
    

def escolhas_buscar():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                nome()
            case 4:
                voltar_ao_menu()
            case 5:
                finalizar_app()
            case _:
                buscar()
    except ValueError:
        buscar()

def nome():
    print("BUsca por nome")

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