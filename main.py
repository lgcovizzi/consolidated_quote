import os
from supermercado import Supermercado
diretorio_raiz = os.getcwd()  # Obtém o diretório de trabalho atual

# Lista todos os arquivos no diretório raiz
arquivos_no_diretorio = os.listdir(diretorio_raiz)

# Filtra os arquivos com a extensão .txt
arquivos_txt = [arquivo for arquivo in arquivos_no_diretorio if arquivo.endswith(".txt")]

# Imprime a lista de arquivos .txt
for arquivo in arquivos_txt:
    # Abra o arquivo em modo de leitura ('r')
    with open(arquivo, 'r') as arquivo:
    # Leia o conteúdo do arquivo
        conteudo = arquivo.read()
        linhas = conteudo.split('\n')  # Divide o conteúdo em linhas
        linhas = [linha for linha in linhas if linha.strip() != ""]
        ultimas_linhas = linhas[-2:]
        produtos = linhas[:-1]

    #print(conteudo)
    print('ultimas linhas: ', ultimas_linhas)

    supermercado=Supermercado(ultimas_linhas, produtos)
    supermercado.Total()

