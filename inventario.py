class Inventario():

    estoque = {}
    def __init__(self):
        pass
    
    #Inicializa um estoque para um certo tipo de produto
    def criar_estoque(self, tipo_produto):
        self.estoque[tipo_produto] = {}

    #Adiciona ao tipo de produto o produto e sua quantidade
    def adicionar_estoque(self, tipo_produto, produto, quantidade_adicionada):
        try:
            quantidade_atual = self.estoque[tipo_produto][produto]
        except:
            quantidade_atual = 0
        self.estoque[tipo_produto][produto] = quantidade_atual + quantidade_adicionada

    def vender(self, tipo_produto, produto, quantidade_vendida):
        try:
            quantidade_atual = self.estoque[tipo_produto][produto]
            if quantidade_atual == 0:
                raise Exception
        except:
            print(f"{produto} está sem estoque.")
        self.estoque[tipo_produto][produto] = quantidade_atual - quantidade_vendida
    
    def __str__(self):
        inventario = ''
        for tipo_produto in self.estoque:
            inventario += f"{tipo_produto}: {self.estoque[tipo_produto]}\n"
        
        return inventario

Inventario = Inventario()
Inventario.criar_estoque("Roupa")
Inventario.criar_estoque("Manga")
Inventario.criar_estoque("Jogo")
Inventario.adicionar_estoque("Roupa","Camiseta azul",3)
Inventario.adicionar_estoque("Roupa","Tênis da nike",5)
Inventario.adicionar_estoque("Manga","Horimia",5)
print(Inventario)