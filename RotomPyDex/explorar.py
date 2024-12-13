import os
import time
import pandas as pd
import titulo
import app

from app import df,exibir_opcoes,escolher_opcao

pagina = 1
linhas_por_pagina=10
total_paginas = (len(df) // linhas_por_pagina) + (len(df) % linhas_por_pagina > 0)

def explorar(): # responsavel pela arquitetura da funçao explorar 
    os.system('cls')
    titulo.titulo()
    opcoes_explorar()
    inicio = (pagina - 1) * linhas_por_pagina
    fim = min(inicio + linhas_por_pagina, len(df))
    print(df[inicio:fim])           
    opcoes_explorar()
    dex()
    
def opcoes_explorar(): #exibe as opções para navegação no app
    print('\n|1 - Proxima|', '|2 - Anterior|', '|3 - Primeira|', '|4 - Ultima|', '|5 - Menu|', '|6 - Sair|\n')
    
def dex():# responsavel por receber um input referente as opcoes_explorar e executar as funções
    print(f'Página {pagina} de {total_paginas}')
        # Calcular o índice de início e fim
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                proxima()
            case 2:
                anterior()
            case 3:
                primeira()
            case 4:
                ultima()
            case 5:
                voltar_ao_menu()
            case 6:
                finalizar_app()
            case _:
                explorar()
    except ValueError:
        explorar()
    
def proxima():
    global pagina
    if pagina < total_paginas:
        pagina += 1
        explorar()
    else:
        print("\nVocê está na última página.")
        time.sleep(1)
        explorar()
        
def anterior():
    global pagina
    if pagina > 1:
        pagina -= 1
        explorar()
    else:
        print("\nVocê está na primeira página.")
        time.sleep(1)
        explorar()
        
def primeira():
    global pagina
    pagina = 1
    explorar()

def ultima():
    global pagina
    pagina = total_paginas
    explorar()

def voltar_ao_menu():
    ''' Retorna ao menu'''
    print('\nVoltando ao menu. ')
    time.sleep(1)
    os.system('cls')
    titulo.titulo()
    exibir_opcoes()
    escolher_opcao()

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