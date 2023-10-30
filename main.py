from inventario import Inventario
from produto import Roupa, Manga, Jogo

from enum import Enum

class Marcas(Enum):
    NIKE = 1
    SUPERCELL = 2
    HINOKAMI = 3

Invent = Inventario()

Invent.criar_estoque("Roupa")
Invent.criar_estoque("Manga")
Invent.criar_estoque("Jogo")

calca = Roupa(100, Marcas.NIKE.name, "Calça", "Preta")
manga1 = Manga(20, Marcas.HINOKAMI.name, "Attack On Titan","Shounen", False)
manga2 = Manga(20, Marcas.HINOKAMI.name, "Attack On Titan","Shounen", True)
subnautica = Jogo(10, Marcas.SUPERCELL.name, "Subnautica", "PC")

Invent.adicionar_estoque(calca, 10)
Invent.adicionar_estoque(manga1, 5)
Invent.adicionar_estoque(manga2, 7)
Invent.adicionar_estoque(subnautica, 1)

Invent.vender(calca, 10)
Invent.vender(manga1, 5)
Invent.vender(manga2, 7)
Invent.vender(subnautica, 1)

print(Invent)

Invent.vender(manga1, 5)

Invent.checar_estoque(manga1)