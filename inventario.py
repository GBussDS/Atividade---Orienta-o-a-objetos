class Inventario():

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

    def vender(self, tipo_produto, produto, quantidade_vendida)
        try:
            quantidade_atual = self.estoque[tipo_produto][produto]
            if quantidade_atual == 0:
                raise Exception
        except:
            print(f"{produto} está sem estoque.")
        self.estoque[tipo_produto][produto] = quantidade_atual - quantidade_vendida

Inventario = Inventario()
Inventario.criar_estoque("Roupa")
Inventario.adicionar_estoque("Roupa","Camiseta azul",3)
Inventario.adicionar_estoque("Roupa","Camiseta azul",5)
print(Inventario.estoque)