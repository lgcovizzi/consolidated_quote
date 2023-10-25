from produto import Produto
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Cambia 'en_US.UTF-8' a tu configuración local

class Supermercado:
  marcador_de_ausencia='Não possui cotação'
  def __init__(self, array_nome_endereco, array_produtos):
    self.array_produtos=array_produtos
    self.array_nome_endereco=array_nome_endereco
    self.nome=''
    self.endereco=''
    self.lista_de_produtos = []
    for parametro in array_nome_endereco:
      try:
        parte1, parte2 = parametro.rsplit("R$", 1)
        parte1, parte2 = parte2.split(" ", 1)
        self.nome=parte2
      except ValueError:
        self.endereco=parametro

    for linha in range (0,len(self.array_produtos),2):
      produto=self.array_produtos[linha]
      preco=self.array_produtos[linha+1]

      titulo, unidade = produto.rsplit("-")
      quantidade_padrao, unidade=unidade.split(" ",1)
      unidade=unidade.strip()
      titulo=titulo.strip()

      if self.marcador_de_ausencia not in preco:
        quantidade, preco = preco.rsplit("R$", 1)
        palavraQuantidade, quantidade=quantidade.rsplit(':', 1)
        quantidade=quantidade.strip()
        quantidade=int(quantidade)
        preco = float(preco.replace(',', '.'))
      else:
        preco=0.0
      
      produto = Produto(preco=preco, quantidade=quantidade, titulo=titulo,unidade=unidade )
      self.lista_de_produtos.append(produto)
      

  def Total(self):
    total=0
    for item in self.lista_de_produtos:     
      total=item.calcular_valor_total()+total
    return locale.currency(total, grouping=True)
  
  def listar_produtos(self):
    lista=[]
    for item in self.lista_de_produtos:
      titulo=item.titulo
      lista.append(titulo)
    return lista

  def listar_precos(self):
    lista=[]
    for item in self.lista_de_produtos:
      preco=locale.currency(item.preco, grouping=True)
      lista.append(preco)
    return lista

  def listar_quantidades(self):
    lista=[]
    for item in self.lista_de_produtos:
      quantidade=item.quantidade
      lista.append(quantidade)
    return lista
  
  def listar_unidades(self):
    lista=[]
    for item in self.lista_de_produtos:
      unidade=item.unidade
      lista.append(unidade)
    return lista
  
  if __name__ == "__main__":
    import subprocess
    # Executar "arquivo2.py" como um processo independente
    subprocess.call(["python", "main.py"])


    

