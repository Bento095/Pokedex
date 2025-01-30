import os
import time
import titulo
import main as main



def voltar_ao_menu(): 
    ''' Retorna ao menu'''
    print('\nVoltando ao menu. ')
    time.sleep(0.5)
    os.system('cls')
    titulo.titulo()
    main.exibir_opcoes()
    main.escolher_opcao()

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
    '''Encerra o app limpando a tela após uma mensagem de encerramento'''

    exibir_subtitulo('Obrigado por testar! ٩(^ᴗ^)۶')
