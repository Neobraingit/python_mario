
with open('archivo.txt', 'r') as archivo:
    contenido  = archivo.read()
    
print (contenido)


with open('archivo.txt', 'w') as archivo:
    archivo.write('Probando a escribir')
    
with open('archivo.txt', 'a') as archivo:
    archivo.write('Respetando lo anterior')
    
with open('archivo.txt', 'r') as archivo:
    for linea in archivo:
        print (linea)