import xml.etree.ElementTree as ET

from piso import Piso
from patron import Patron
from nodo import Nodo
from listaDoble import ListaDoble
import os

listaD = ListaDoble()
auxiliar = ''
floor = ''
p = ''

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
    global auxiliar
    global floor
    global p
    print("Ingrese nombre de Piso: ")
    p = str(input('>'))
    floor = listaD.buscar(p)
    print(floor)
    print("Ingrese código de Patron: ")
    codigo = str(input('>'))
    auxiliar = listaD.buscarPatron(p, codigo)
    print(auxiliar)


def buscarNuevoPatron():
    global p
    global auxiliar
    print("Ingrese nuevo código de Patron: ")
    codigo = str(input('>'))
    auxiliar = listaD.buscarPatron(p, codigo)
    print(auxiliar)

def graficar():
    global auxiliar
    global floor
    cadena = ''
    file = open('Grafica.dot', 'w')
    cadena = cadena + 'digraph G { bgcolor="pink"\n'
    cadena = cadena + 'fontname="Helvetica,Arial,sans-serif" \n'
    cadena = cadena + 'node [fontname="Helvetica,Arial,sans-serif"] \n'
    cadena = cadena + 'edge [fontname="Helvetica,Arial,sans-serif"] \n'
    cadena = cadena + 'a0 [shape = "none", label=< \n'
    cadena = cadena + '<TABLE border="2" cellspacing="2" cellpadding="10" bgcolor="mediumpurple1"> \n'
    caracter = 0
    while caracter < len(auxiliar.secuencia):
        for i in range(1 , int(floor.filas)+1):
            cadena = cadena + '<TR> \n'
            for j in range(1, int(floor.columnas)+1):
                if auxiliar.secuencia[caracter] == 'B':
                    cadena = cadena + '<TD border="1"  bgcolor="black"  gradientangle="270">'+ '</TD>\n'
                else:
                    cadena = cadena + '<TD border="1"  bgcolor="white"  gradientangle="270">'+ '</TD>\n'
                caracter += 1 
            cadena = cadena + '</TR>\n'
    cadena = cadena + '</TABLE>>];\n'
    cadena = cadena + '}\n'
    file.write(cadena)
    file.close()
    os.system('dot -Tpng Grafica.dot -o Grafica.png')
    os.startfile(os.path.normpath('Grafica.png')) 


def bubble_sort(our_list):
    for i in range(len(our_list)):
        for j in range(len(our_list) - 1):
            if our_list[j].codigo > our_list[j+1].codigo:
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

def imprimirOrdenar():
    print('------------------------Lista Ordenada:----------------------------')
    listaD.ordenar()
    actual = listaD.primero
    while actual is not None:
        bubble_sort(actual.piso.patrones)
        actual = actual.siguiente
    listaD.recorrer()



    





    
