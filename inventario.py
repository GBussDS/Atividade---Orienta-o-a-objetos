from produto import Roupa, Manga, Jogo

class Inventario():

    def __init__(self):
        self.estoque = {}
        self.receita = 0
    
    #Inicializa um estoque para um certo tipo de produto
    def criar_estoque(self, tipo_produto):
        self.estoque[tipo_produto] = {}

    #Adiciona ao tipo de produto o produto e sua quantidade
    def adicionar_estoque(self, produto, quantidade_adicionada):

        #Pega as propriedades do produto colocar no estoque
        tipo_produto = produto.get_categoria()
        produto = produto.get_nome_estoque()

        try:
            if produto not in self.estoque[tipo_produto]:
                self.estoque[tipo_produto][produto] = 0
        
            quantidade_atual = self.estoque[tipo_produto][produto]

            self.estoque[tipo_produto][produto] = quantidade_atual + quantidade_adicionada
        except KeyError:
            print("Não existe estoque para esse tipo de produto ainda!")
        

    #Remove uma certa quantidade do produto do estoque e adiciona o dinheiro recebido a receita.
    def vender(self, produto, quantidade_vendida):

        tipo_produto = produto.get_categoria()
        preco = produto.get_preco()
        produto = produto.get_nome_estoque()

        try:
            quantidade_atual = self.estoque[tipo_produto][produto]
            if quantidade_atual == 0:
                raise KeyError
            if quantidade_atual < quantidade_vendida:
                raise ValueError
            self.estoque[tipo_produto][produto] = quantidade_atual - quantidade_vendida
            self.receita += preco*quantidade_vendida

        except KeyError:
            print(f"{produto} está sem estoque.")
        except ValueError:
            print("Quantidade vendida é maior que quantidade em estoque.")
    
    def retorno(self, produto, quantidade_retornada):

        tipo_produto = produto.get_categoria()
        preco = produto.get_preco()
        produto = produto.get_nome_estoque()

        try:
            quantidade_atual = self.estoque[tipo_produto][produto]
            if self.receita < quantidade_retornada * preco:
                raise ValueError
            self.estoque[tipo_produto][produto] = quantidade_atual + quantidade_retornada
            self.receita -= preco*quantidade_retornada

        except KeyError:
            print("Não existe estoque para esse produto.")
        except ValueError:
            print("Quantidade a ser retornada ultrapassa a receita atual.")
    
    def checar_estoque(self, produto):

        tipo_produto = produto.get_categoria()
        produto = produto.get_nome_estoque()

        try:
            quantidade_atual = self.estoque[tipo_produto][produto]
    
            if quantidade_atual == 0:
                raise KeyError

            print(f"Ainda restam {quantidade_atual} unidades do produto '{produto}' em estoque.")
        except KeyError:
            print(f"{produto} está sem estoque.")
    
    #Passa a printar uma linha para cada tipo de produto.
    def __str__(self):
        inventario = f"Receita atual: {self.receita}\n"
        for tipo_produto in self.estoque:
            inventario += f"{tipo_produto}: {self.estoque[tipo_produto]}\n"
        
        return inventario
