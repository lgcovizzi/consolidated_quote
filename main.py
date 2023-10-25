import os
from supermercado import Supermercado
diretorio_raiz = os.getcwd()  # Obtém o diretório de trabalho atual
supermercados=[]
relatorio_cabecalho_1=['item', 'descrição', "quantidade",'unidade']
relatorio_cabecalho_2=['', '','','']
# Lista todos os arquivos no diretório raiz
arquivos_no_diretorio = os.listdir(diretorio_raiz)

# Filtra os arquivos com a extensão .txt
arquivos_txt = [arquivo for arquivo in arquivos_no_diretorio if arquivo.endswith(".txt")]
relatorio=[]
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

    supermercado=Supermercado(ultimas_linhas, produtos)
    supermercados.append(supermercado)

for i in range (0, len(supermercados),1):
    relatorio_cabecalho_1.append(supermercados[i].nome)
    relatorio_cabecalho_2.append(supermercados[i].endereco)

relatorio.append(relatorio_cabecalho_1)
relatorio.append(relatorio_cabecalho_2)

lista_de_produtos=supermercados[0].listar_produtos()
lista_de_quantidades=supermercados[0].listar_quantidades()
lista_de_unidades=supermercados[0].listar_unidades()

for j in range(0, len(lista_de_produtos)):    
    linha=[j+1, lista_de_produtos[j],lista_de_quantidades[j],lista_de_unidades[j]]
    for k in range (0, len(supermercados),1):
        linha.append(supermercados[k].listar_precos()[j])
    relatorio.append(linha)
linha=[]
linha=['','','','Total']

for l in range (0, len(supermercados),1):    
    linha.append(supermercados[l].Total())
relatorio.append(linha)

# Nome do arquivo de texto que você deseja criar
nome_arquivo = 'resultado.csv'

# Abrir o arquivo de texto em modo de escrita
with open(nome_arquivo, 'w') as arquivo:
    for array in relatorio:
        linha = ';'.join(map(str, array))  # Converter os elementos do array em uma única string separada por vírgulas
        arquivo.write(f'{linha}\n')  # Escrever a linha no arquivo e adicionar uma quebra de linha

print(f'O arquivo de texto "{nome_arquivo}", separando por ponto e vírgula.')

