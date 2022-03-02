class Patron:
    
    def __init__(self, codigo, secuencia):
        self.codigo = codigo
        self.secuencia = secuencia
        

    def __str__(self) -> str:
        return "{" + str(self.codigo) + " - " + str(self.secuencia) + "}"