marcador_de_negacao='Não possui cotação para o mercado selecionado.'

from produto import Produto


class Item:
    def __init__(self, linha1, linha2):
        self.linha1 = linha1
        self.linha2 = linha2
        
    def retornar_produto(self):
        
        titulo=""
        preco=0.0
        quantidade=0
        unidade=''

        # 1                               ABACAXI PEROLA -1 UN
        titulo, unidade_composta = self.linha1.rsplit("-", 1)
        _quantidade, unidade  = unidade_composta.split(" ")
        titulo=titulo.rstrip()

        if marcador_de_negacao != self.linha2:
            quantidade_solicitada_string, preco_string = self.linha2.split(" ",1)
            # 2                              Quantidade:1 R$ 7,49
            _quantidade, quantidade =quantidade_solicitada_string.split(":")
            quantidade=int(quantidade)
            moeda, preco=preco_string.split(" ")
            preco=float(preco.replace(",", "."))

        print(_quantidade)
        produto = Produto(titulo=titulo, preco=preco,quantidade=quantidade,unidade=unidade)
        return produto


if __name__ == "__main__":
    item = Item("ABACATE -1 KG", "Quantidade:2 R$ 7,49")
    print(item.retornar_produto())



#                                            ABACATE -1 KG
# 0                              Quantidade:1 R$ 3,99 
# 1                               ABACAXI PEROLA -1 UN
# 2                              Quantidade:1 R$ 7,49 
# 3                                TOMATE CEREJA -1 KG
# 4                             Quantidade:1 R$ 10,39 
# 5   ACHOCOLATADO EM PÓ INSTANTÂNEO -SHOWCAU -1,01 KG
# 6    Não possui cotação para o mercado selecionado. 
# 7    ACHOCOLATADO EM PÓ INSTANTÂNEO -SHOWCAU -370 GR
# 8  Não possui cotação para o mercado selecionado....
# Conteúdo da aba Planilha1:
#                                        ABACATE -1 KG
# 0                              Quantidade:1 R$ 3,99 
# 1                               ABACAXI PEROLA -1 UN
# 2                              Quantidade:1 R$ 7,49 
# 3                                TOMATE CEREJA -1 KG
# 4                             Quantidade:1 R$ 10,39 
# 5   ACHOCOLATADO EM PÓ INSTANTÂNEO -SHOWCAU -1,01 KG
# 6    Não possui cotação para o mercado selecionado. 
# 7    ACHOCOLATADO EM PÓ INSTANTÂNEO -SHOWCAU -370 GR
# 8  Não possui cotação para o mercado selecionado....