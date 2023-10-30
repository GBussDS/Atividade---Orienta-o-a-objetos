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

    #Remove uma certa quantidade do produto do estoque.
    def vender(self, tipo_produto, produto, quantidade_vendida):
        try:
            quantidade_atual = self.estoque[tipo_produto][produto]
            if quantidade_atual == 0:
                raise KeyError
            if quantidade_atual < quantidade_vendida:
                raise ValueError
            self.estoque[tipo_produto][produto] = quantidade_atual - quantidade_vendida

        except KeyError:
            print(f"{produto} está sem estoque.")
        except ValueError:
            print("Quantidade vendida é maior que quantidade em estoque.")
    
    def checar_estoque(self, tipo_produto, produto):
        try:
            quantidade_atual = self.estoque[tipo_produto][produto]
    
            if quantidade_atual == 0:
                raise KeyError

            print(f"Ainda restam {quantidade_atual} unidades do produto '{produto}' em estoque.")
        except KeyError:
            print(f"{produto} está sem estoque.")
    
    #Passa a printar uma linha para cada tipo de produto.
    def __str__(self):
        inventario = ""
        for tipo_produto in self.estoque:
            inventario += f"{tipo_produto}: {self.estoque[tipo_produto]}\n"
        
        return inventario

Inventario = Inventario()
Inventario.criar_estoque("Roupa")
Inventario.criar_estoque("Manga")
Inventario.criar_estoque("Jogo")
Inventario.adicionar_estoque("Roupa","Camiseta azul",3)
Inventario.adicionar_estoque("Roupa","Tênis da nike",5)
Inventario.checar_estoque("Roupa","Tênis da nike")
Inventario.vender("Roupa","Tênis da nike",5)
Inventario.checar_estoque("Roupa","Tênis da nike")
Inventario.vender("Roupa","Tênis da nike",5)
print(Inventario)