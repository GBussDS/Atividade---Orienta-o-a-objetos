class Produto:

    #Atributo estatico
    codigo_barras_atual = 0

    def __init__(self, categoria, preco):
        self.categoria = categoria
        Produto.codigo_barras_atual = Produto.codigo_barras_atual + 1
        self.codigo_de_barras = Produto.codigo_barras_atual
        self.preco = preco
    
    #Retorna o código de barras
    def get_codigo_de_barras(self):
        return self.codigo_de_barras

    #Retorna o preço
    def get_preco(self):
        return self.preco

    #Define como o produto vai ser printado
    def __str__(self):
        return f"Produto do tipo: {self.categoria}. Código de barras: {self.codigo_de_barras}\n"

class Roupa(Produto):

    def __init__(self, preco, tipo, cor, marca):
        super().__init__("Roupa", preco)
        self.tipo = tipo
        self.cor = cor
        self.marca = marca

    def vestir(self):
        print(f"Você está vestindo {self.tipo} da cor {self.cor} da marca {self.marca}.\n")

class Manga(Produto):

    def __init__(self, preco, titulo, autor, genero, bTraduzido):
        super().__init__("Manga", preco)
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.bTraduzido = bTraduzido

    def ler(self):
        if self.bTraduzido == "sim" or self.bTraduzido:
            print(f"Você está lendo {self.titulo}, que é um {self.genero} escrito por {self.autor}.\n")
        else:
            print(f"Você está lendo {self.titulo}, que é um {self.genero} escrito por {self.autor}.")
            print("Como você sabe japonês?\n")

class Jogo(Produto):
    
    def __init__(self, preco, nome, console, ano_lancamento):
        super().__init__("Jogo", preco)
        self.nome = nome
        self.console = console
        self.ano_lancamento = ano_lancamento

    def jogar(self):
        print(f"Você está jogando {self.nome} lançado em {self.ano_lancamento} em um {self.console}.\n")

# calca = Roupa(100, "Calça", "Preta", "Nike")
# anime = Manga(20, "Attack On Titan", "Hajime Isayama", "Shounen", False)
# clashroyale = Jogo(10, "Clash Royale", "Android", 2016)