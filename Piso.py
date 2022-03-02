class Piso:

    def __init__(self, nombre, filas, columnas, costoVolteo, costoIntercambio, patrones = []):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.costoVolteo = costoVolteo
        self.costoIntercambio = costoIntercambio
        self.patrones = patrones


    def __str__(self) -> str:
        patron = ''
        for pat in self.patrones:
            patron += str(pat)
        return "{" + str(self.nombre) + ", " + str(self.filas) + ", " + str(self.columnas) + ", " + str(self.costoVolteo) + ", " + str(self.costoIntercambio) + ", " +  "{ " + patron + "} " + "}" 