from nodo import Nodo
from patron import Patron

class ListaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None


    def insertarPiso(self, Piso):
        if self.primero is None:
            self.primero = self.ultimo = Nodo(Piso)
        else: 
            actual = self.ultimo
            self.ultimo = actual.siguiente = Nodo(Piso)
            self.ultimo.anterior = actual
            

    def recorrer(self):
        actual = self.primero
        while actual:
            print(actual.piso)
            actual = actual.siguiente
        

    def buscar(self, piso):
        if self.primero is None:
            return
        actual = self.primero
        while actual:
            if actual.piso.nombre == piso:
                return actual.piso
            actual = actual.siguiente

    
    def buscarPatron(self, piso, patron):
        if self.primero is None:
            return
        actual = self.primero
        while actual:
            if actual.piso.nombre == piso:
                for p in actual.piso.patrones:
                    if p.codigo == patron:
                        return p
                return actual.piso
            actual = actual.siguiente


    def ordenar(self):
        nombres = []
        if self.primero is None:
            return
        actual = self.primero
        for name in actual.piso:
            name = actual.piso.nombre
            nombres.append(name)
        return