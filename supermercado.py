from produto import Produto
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Cambia 'en_US.UTF-8' a tu configuración local

class Supermercado:
  marcador_de_ausencia='Não possui cotação'
  def __init__(self, array_nome_endereco, array_produtos):
    self.array_produtos=array_produtos
    self.array_nome_endereco=array_nome_endereco
    self.nome=array_nome_endereco[0]
    self.endereco=array_nome_endereco[1]
    self.lista_de_produtos = []

    for linha in range (0,len(self.array_produtos), 1):

      preco=0.0
      quantidade=0
      titulo=''
      unidade="UNI"
      adicionar=False

      
      #tentar o primeira linha
      try:
        _produto_unidade_padrao=self.array_produtos[linha]    
        titulo, quantidade_padrao = _produto_unidade_padrao.rsplit("-",1)
        unidade=quantidade_padrao.strip()
        titulo=titulo.strip()
      except:
        print('An exception occurred')
      
      # tentar segunda linha
      try:
        _quantidade=self.array_produtos[linha + 1]                
        quantidade=int(_quantidade.rsplit(":",1)[1])
        
      except:
        print('An exception occurred')

      #tentar terceira linha
      try:
        _preco=self.array_produtos[linha + 2]
        _preco=_preco.rsplit(" ",1)[1]
        preco=float(_preco.replace(',', '.'))
        adicionar=True
      except:
        print('An exception occurred')

      if adicionar:
        produto=Produto(titulo=titulo, quantidade=quantidade, preco=preco, unidade=unidade)
        self.lista_de_produtos.append(produto)
      
      try:
        if self.marcador_de_ausencia in self.array_produtos[linha + 1]  :
          produto=Produto(titulo=titulo, quantidade=quantidade, preco=preco, unidade=unidade)
          self.lista_de_produtos.append(produto)
      except:
        print('An exception occurred')

      
      
      

  def Total(self):
    total=0
    for item in self.lista_de_produtos:     
     total=item.preco + total
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


    

