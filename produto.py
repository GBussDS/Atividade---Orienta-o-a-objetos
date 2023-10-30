class Produto:

    def __init__(self, tipo, codigo_de_barras):
        self.tipo = tipo
        self.codigo_de_barras
    
    #Retorna o código de barras
    def get_codigo_de_barras(self):
        return self.codigo_de_barras

    #Define como o produto vai ser printado
    def __str__(self):
        return f"Produto do tipo: {self.tipo} com código de barras: {self.codigo_de_barras}"