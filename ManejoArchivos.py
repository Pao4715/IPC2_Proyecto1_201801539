from xml.dom import minidom



archivo = minidom.parse('ejemplo.xml')
nombre = archivo.getEelementsByTagName('piso')
nombres = []
for n in nombre:
    patrones = n.getElementsByTagName('codigo')
    filas = n.getAttribute('R')
    columnas = n.getAttribute('C')
