class Iventario():

    estoque = {}
    def __init__(self):
        pass
    
    def criar_estoque(self, tipo_produto):
        self.estoque[tipo_produto] = {}
    
    def adicionar_estoque(self, tipo_produto, produto, quantidade_adicionada):
        try:
            quantidade_atual = self.estoque[tipo_produto][produto]
        except:
            quantidade_atual = 0
        self.estoque[tipo_produto][produto] = quantidade_atual + quantidade_adicionada

Iventario = Iventario()
Iventario.criar_estoque("Roupa")
Iventario.adicionar_estoque("Roupa","Camiseta azul",3)
Iventario.adicionar_estoque("Roupa","Camiseta azul",5)
print(Iventario.estoque)