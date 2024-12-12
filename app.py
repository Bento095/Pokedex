import os
import pandas as pd
import time
import explorar
import buscar
import titulo

from explorar import *
from buscar import *

df = pd.read_csv(r'C:\Users\Shiryu EVA UNIT-GE\Documents\Pokedex\pkm.csv', index_col=False)
df.drop(df.columns[-1], axis=1, inplace=True)

def exibir_opcoes():
    print('1. Explorar')
    print('2. Buscar')
    print('3. Sair\n')

def opcao_invalida():
    '''Exibe uma mensagem de opção invalida e retorna ao menu ao clicar a proxima tecla.

    Outputs:
    - Retorna ao menu principal'''

    print('Opçao invalida\n')
    voltar_ao_menu()

def escolher_opcao():
    '''Utiliza  o input escolhido para executar a função corespondente, incuindo opção invalida
    
    Outputs:
    - Executa a opção ecolhida'''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                explorar.explorar()
            case 2:
                buscar()
            case 3:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

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
    
# Bloco principal do programa
def main():
    os.system('cls')
    titulo.titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
    # Código que será executado quando o programa é iniciado
    # Executa as funções, processa dados, etc.