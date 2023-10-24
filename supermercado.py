marcador_de_planilha='Planilha'
import pandas as pd

from produto import Produto

class Supermercado:
  def __init__(self, df):
    self.df=df
    ultimas_duas_linhas = df.tail(2)
    self.endereco= df.tail(1)
    self.titulo = df.iloc[-2]
    novo_df = pd.concat([ultimas_duas_linhas])
    df_string = novo_df.to_string(index=False)
#"Não possui cotação para o mercado selecionado. Total: R$9,87 ASSAÍ ATACADISTA - ATUBA
#                                                 BR 4761, 1801 - Atuba - Curitiba/PR"
    parte1, parte2 = df_string.split("R$", 1)
    parte2=parte2.split(" ",1)
    self.titulo, self.endereco=parte2[1].split('\n')
    self.endereco=self.endereco.lstrip()
    
    #print(self.titulo)
    #print(self.endereco)

  def listar_produtos(self):
    for i in range(1, len(self.df), 2):
      #result=self.df.loc[i].split(" ")
      print("produto 1:", self.df.loc[i].to_string(index=True))
      print("produto 2:", self.df.loc[i+1].to_string(index=True))

  def imprimir_produtos(self):
    print(self.df)

  def mostrar_titulo(self):
    for linha in self.linhas:
      print(linha)

  def mostrar_endereco(self):
    print(self.endereco)


  #if __name__ == "__main__":
    

