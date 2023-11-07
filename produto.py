



class Produto:
    def __init__(self, titulo :str, unidade :str, quantidade :int, preco_unitatio :float):
        self.titulo = titulo
        self.unidade = unidade
        self.quantidade = quantidade
        self.preco_unitatio = preco_unitatio
        _preco_total=0
        try:
          _preco_total=quantidade*preco_unitatio
        except:
          pass
        
        self.preco_total=_preco_total


    def __str__(self):
        return f"Produto: {self.titulo}\nUnidade: {self.unidade}\nQuantidade: {self.quantidade}\nPreço: R${self.preco_unitatio:.2f}\nValor Total: R${self.preco_total:.2f}"

if __name__ == "__main__":
   produto=Produto("Batata", "KG", 1, 3.4)
   print(produto)

#tipos de entradas
# FARINHA DE TRIGO -( + ) BARATO -1 KG
# Quantidade:4
# R$ 19,16
# LEITE INTEGRAL 3% DE GORDURA -SANTA CLARA -1 LITRO
# Não possui cotação para o mercado selecionado.
