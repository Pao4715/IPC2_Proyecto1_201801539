import xml.etree.ElementTree as ET
from piso import Piso
from patron import Patron
from nodo import Nodo
from listaDoble import ListaDoble

listaD = ListaDoble()

def extraerDatos():

    print('Ingrese ruta del archivo xml')
    archivo = str(input('>>'))
    xmldoc = ET.parse(archivo)

    rect = {}
    nombre = ''
    filas = 0
    columnas = 0
    costoVoltear = 0
    costoIntercambiar = 0

    raiz = xmldoc.getroot()

    for piso in raiz.iter('piso'):
        nombre = piso.get('nombre')
        
        for r in piso.iter('R'):
            rect['R'] = r.text
            filas = rect['R']
        
        for c in piso.iter('C'):
            rect['C'] = c.text
            columnas = rect['C']
        
        for f in piso.iter('F'):
            rect['F'] = f.text
            costoVoltear = rect['F']
        
        for s in piso.iter('S'):
            rect['S'] = s.text
            costoIntercambiar = rect['S']
        
        for pat in piso.iter('patrones'):
            patrones = []
            
            for patron in pat.iter('patron'):
                codigo = patron.get('codigo')

                rect['patron'] = patron.text
                textoPatron = rect['patron'].strip()

                patronNuevo = Patron(codigo, textoPatron)
                patrones.append(patronNuevo)
                

        nuevoPiso = Piso(nombre, filas, columnas, costoVoltear, costoIntercambiar, patrones)
        listaD.insertarPiso(nuevoPiso)
    listaD.recorrer()


def mostrarBuscar():
    print("Ingrese nombre de Piso: ")
    p = str(input('>'))
    print(listaD.buscar(p))

def mostrarBuscarPatron():
    print("Ingrese nombre de Piso: ")
    p = str(input('>'))
    print(listaD.buscar(p))
    print("Ingrese código de Patron: ")
    codigo = str(input('>'))
    print(listaD.buscarPatron(p, codigo))

    





    
