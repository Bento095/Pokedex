import os
import pandas as pd
import time
import explorar
import buscar
import titulo
import voltar as voltar


df = pd.read_csv('RotomPyDex\pkm.csv', index_col=False)
df.drop(df.columns[-1], axis=1, inplace=True)

def exibir_opcoes():
    print('1. Explorar')
    print('2. Buscar')
    print('3. Sair\n')

def opcao_invalida():
    '''Exibe uma mensagem de opção invalida e retorna ao menu ao clicar a proxima tecla.'''

    print('Opçao invalida\n')
    time.sleep(0.5)

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
                buscar.buscar()
            case 3:
                voltar.finalizar_app()
            case _:
                voltar.opcao_invalida()
                voltar.voltar_ao_menu()
    except ValueError:
        opcao_invalida()
        voltar.voltar_ao_menu()


    
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