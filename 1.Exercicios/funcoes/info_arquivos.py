#3. Implementar uma função que leia um arquivo e retorne uma lista de tuplas
#com os dados (o separador de campo do arquivo é vírgula), eliminando as
#linhas vazias. Caso ocorra algum problema, imprima uma mensagem de
#aviso e encerre o programa.

def info_txt(caminho):
    try:
        with open(caminho, 'r'):
            linhas = caminho.readlines()
            linhas = [linha.strip() for linha in linhas if linhas.strip()]
            dados = [tuple(linhas.split(',')) for linha in linhas]
            return dados
    except FileExistsError:
        print(f'Arquivo {caminho} não encontrado.')
    except Exception as e:
        print(f'Erro inesperado: {e}')
    finally:
        print('Programa encerrado.')


nome_do_arquivo = input('Caminho para o arquivo arquivo: ')
dados_lidos = info_txt(nome_do_arquivo)
print(dados_lidos)