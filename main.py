from inventario import Inventario
from produto import Roupa, Manga, Jogo

from enum import Enum

class Marcas(Enum):
    NIKE = 1
    SUPERCELL = 2
    HONOKAMI = 3

estoque = Inventario()

estoque.criar_estoque("Roupa")
estoque.criar_estoque("Manga")
estoque.criar_estoque("Jogo")

calca = Roupa(100, "Nike", "Calça", "Preta")
manga1 = Manga(20, "Anime", "Attack On Titan","Shounen", False)
manga2 = Manga(20, "Anime", "Attack On Titan","Shounen", True)
subnautica = Jogo(10, "naosei", "Subnautica", "PC")

estoque.adicionar_estoque(calca, 10)
estoque.adicionar_estoque(manga1, 5)
estoque.adicionar_estoque(manga2, 7)
estoque.adicionar_estoque(subnautica, 1)

print(estoque)

estoque.vender(subnautica, 1)

estoque.checar_estoque(subnautica)