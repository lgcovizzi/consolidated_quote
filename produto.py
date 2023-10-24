



class Produto:
    def __init__(self, titulo, unidade, quantidade, preco):
        self.titulo = titulo
        self.unidade = unidade
        self.quantidade = quantidade
        self.preco = preco

    def calcular_valor_total(self):
        return self.quantidade * self.preco

    def __str__(self):
        return f"Produto: {self.titulo}\nUnidade: {self.unidade}\nQuantidade: {self.quantidade}\nPreço: R${self.preco:.2f}\nValor Total: R${self.calcular_valor_total():.2f}"


