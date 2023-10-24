import pandas as pd
from supermercado import Supermercado

# Substitua 'seuarquivo.xlsx' pelo nome do seu arquivo Excel
arquivo_excel = '/home/lg/dev/python/cotacao/consolidated_quote/modelo_de_cotacao.xlsx'

# Use o método read_excel para ler o arquivo XLS
# O parâmetro sheet_name=None importará todas as abas
dfs = pd.read_excel(arquivo_excel, sheet_name=None)

# A variável "dfs" conterá um dicionário onde as chaves são os nomes das abas
# e os valores são DataFrames do pandas correspondentes às abas.

# Você pode acessar os DataFrames individuais por meio das chaves do dicionário
for aba, df in dfs.items():
    #print(f'Conteúdo da aba {aba}:')
    #print(df)
    supermercado=Supermercado(df=df)
    supermercado.listar_produtos()

