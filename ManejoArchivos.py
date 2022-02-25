import xml.etree.ElementTree as ET
from Piso import Piso
from patron import Patron

rect = {}
pisos = []
patrones = []

xmldoc = ET.parse('ejemplo.xml')
raiz = xmldoc.getroot()
#print(raiz.tag)

for piso in raiz.iter('piso'):
    nombre = piso.get('nombre')
    #print('Nombre: ',piso.get('nombre'))
    
    for r in piso.iter('R'):
        rect['R'] = r.text
        filas = rect['R']
        #print('Filas: ', rect['R'])
    
    for c in piso.iter('C'):
        rect['C'] = c.text
        columnas = rect['C']
        #print('Columnas: ', rect['C'])
    
    for f in piso.iter('F'):
        rect['F'] = f.text
        costoVoltear = rect['F']
        #print('Costo Voltear: ', rect['F'])
    
    for s in piso.iter('S'):
        rect['S'] = s.text
        costoIntercambiar = rect['S']
        #print('Costo Intercambiar: ', rect['S'])
    
    for pat in piso.iter('patrones'):
        
        for patron in pat.iter('patron'):
            codigo = patron.get('codigo')
            #print('Codigo: ',patron.get('codigo'))
            rect['patron'] = patron.text
            textoPatron = rect['patron']
            #print('patron: ', rect['patron'].strip())

            patronNuevo = Patron(codigo, textoPatron)
            patrones.append(patronNuevo)
            print(patrones)

    nuevoPiso = Piso(nombre, filas, columnas, costoVoltear, costoIntercambiar, patrones)
    pisos.append(nuevoPiso)
print(pisos)

    
