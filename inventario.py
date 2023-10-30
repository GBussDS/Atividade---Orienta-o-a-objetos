from produto import Roupa, Manga, Jogo

class Inventario():

    estoque = {}

    def __init__(self):
        pass
    
    #Inicializa um estoque para um certo tipo de produto
    def criar_estoque(self, tipo_produto):
        self.estoque[tipo_produto] = {}

    #Adiciona ao tipo de produto o produto e sua quantidade
    def adicionar_estoque(self, produto, quantidade_adicionada):

        tipo_produto = produto.get_categoria()

        if produto.get_categoria() == "Roupa":
            produto = f"{produto.get_tipo()} {produto.get_cor()}"

        elif produto.get_categoria() == "Manga":
            produto = f"{produto.get_titulo()}"

        elif produto.get_categoria() == "Jogo":
            produto = f"{produto.get_nome()} {produto.get_console()}"

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

calca = Roupa(100, "Nike", "Calça", "Preta")
anime = Manga(20, "Anime", "Attack On Titan","Shounen", False)
anime2 = Manga(20, "Anime", "Attack On Titan","Shounen", True)
clashroyale = Jogo(10, "supercell", "Clash Royale", "Android")

Inventario.adicionar_estoque(calca, 10)
Inventario.adicionar_estoque(anime, 10)
Inventario.adicionar_estoque(anime2, 5)
Inventario.adicionar_estoque(clashroyale, 2)

print(Inventario)