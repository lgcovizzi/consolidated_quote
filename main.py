import os

from supermercado import Supermercado

diretorio_raiz = os.getcwd()  # Obtém o diretório de trabalho atual


# Lista todos os arquivos no diretório raiz
arquivos_no_diretorio = os.listdir(diretorio_raiz)

#verificar se existe um arquivo de resultados na raiz e remove
if os.path.exists("resultado.csv"):
    os.remove("resultado.csv")


# Filtra os arquivos com a extensão .txt
arquivos_txt = [arquivo for arquivo in arquivos_no_diretorio if arquivo.endswith(".txt")]
relatorio=[]

cabecalho=['item', 'descricao','quantidade',	'unidade' ]
endereco=['','','','',]

relatorio.append(cabecalho)
relatorio.append(endereco)



lista_de_supermercados=[]
for arquivo in arquivos_txt:
    # Abra o arquivo em modo de leitura ('r')
    with open(arquivo, 'r') as arquivo:
        
    # Leia o conteúdo do arquivo
        conteudo = arquivo.read()
        linhas = conteudo.split('\n')  # Divide o conteúdo em linhas
        linhas = [linha for linha in linhas if linha.strip() != ""]
        ultimas_linhas = linhas[-2:]
        produtos = linhas[:-3]
        supermercado=Supermercado(ultimas_linhas, produtos)
        lista_de_supermercados.append(supermercado)
        
for supermercado in lista_de_supermercados:
    cabecalho.append(supermercado.titulo)
    endereco.append(supermercado.local)

lista_de_quantidade_final=lista_de_supermercados[0].listar_quantidades()
for supermercado in range (0,len(lista_de_supermercados), 1):
    lista_de_quantidades=lista_de_supermercados[supermercado].listar_quantidades()
    for item in range (0,len(lista_de_quantidade_final), 1):
      if lista_de_quantidade_final[item]!=lista_de_quantidades[item]:
          lista_de_quantidade_final.insert(item,lista_de_quantidades[item] )
      

lista_de_produtos=lista_de_supermercados[0].lista_de_itens()
lista_de_unidades=lista_de_supermercados[0].listar_unidades()

for item in range (0,len(lista_de_produtos), 1):
    linha=[item + 1]
    linha.append(lista_de_produtos[item])
    linha.append(lista_de_unidades[item])
    linha.append(lista_de_quantidade_final[item])
    for supermercado in range (0,len(lista_de_supermercados), 1):
      lista_de_precos = lista_de_supermercados[supermercado].lista_de_preco()
      linha.append(lista_de_precos[item])
      pass
    relatorio.append(linha)


linha=['','','','Total']

for l in range (0, len(lista_de_supermercados),1):    
    linha.append(lista_de_supermercados[l].somar_precos())
relatorio.append(linha)


# Nome do arquivo de texto que você deseja criar
nome_arquivo = 'resultado.csv'

# Abrir o arquivo de texto em modo de escrita
with open(nome_arquivo, 'w') as arquivo:
    for array in relatorio:
        linha = ';'.join(map(str, array))  # Converter os elementos do array em uma única string separada por vírgulas
        arquivo.write(f'{linha}\n')  # Escrever a linha no arquivo e adicionar uma quebra de linha

if __name__ == "__main__":
   print("feito")