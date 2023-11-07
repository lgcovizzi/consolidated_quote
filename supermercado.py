from produto import Produto

import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Cambia 'en_US.UTF-8' a tu configuración local

class Supermercado:
  marcador_de_ausencia='Não possui cotação'
  def __init__(self, titulo, produtos):
    self.titulo=titulo[0].rsplit("-",1)[0]
    self.local=titulo[1]
    self.produtos=produtos
    self.lista_de_produtos=[]

    for linha in range (0,len(self.produtos), 1):
    
      preco=0.0
      quantidade=0
      titulo=''
      unidade="UNI"
      adicionar=False

      #tentar o primeira linha
      try:
        _produto_unidade_padrao=self.produtos[linha]
        titulo, unidade = _produto_unidade_padrao.rsplit("-",1)   
        
      except:
        pass

      # tentar segunda linha
      try:
        _quantidade=self.produtos[linha + 1]                
        quantidade=int(_quantidade.split(":",1)[1])

      except:
        pass

        #tentar terceira linha
      try:
        _preco=self.produtos[linha + 2]
        _preco=_preco.rsplit(" ",1)[1]
        preco=float(_preco.replace(',', '.'))
        adicionar=True
      except:
        pass

      try:
        if self.marcador_de_ausencia in self.produtos[linha + 1]  :
          adicionar=True
      except:
        pass

      if adicionar:
        produto=Produto(titulo=titulo, unidade=unidade, quantidade=quantidade, preco_unitatio=preco)
        self.lista_de_produtos.append(produto)
      
      self.lista_de_produtos= sorted(self.lista_de_produtos, key=lambda x: x.titulo)
      
    

  
  def contar_itens(self):
    print(len(self.lista_de_produtos))
  

  def somar_precos(self):
    total=0
    for item in self.lista_de_produtos:     
     total=item.preco_total + total
    return locale.currency(total, grouping=True)
  
  def lista_de_itens(self):
    lista=[]
    for item in self.lista_de_produtos:
      titulo=item.titulo
      lista.append(titulo)
    return lista

  def lista_de_preco(self):
    lista=[]
    for item in self.lista_de_produtos:
      preco=locale.currency(item.preco_total, grouping=True)
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

  def nome(self):
    return self.titulo

  def endereco(self):
    return self.local

  
  if __name__ == "__main__":
    import subprocess
    # Executar "arquivo2.py" como um processo independente
    subprocess.call(["python", "main.py"])

