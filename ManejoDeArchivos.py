from io import open
import pathlib

#Abrir archivo

def crearArchivo(nombre):
    ruta = str(pathlib.Path().absolute()) + "/" + nombre
    archivo = open(ruta,"a+")
    archivo.close()

def imprimePersona(campos):

    print(f"\nId: {campos[0]} \t Nombre: {campos[1]} \t CI: {campos[2]}")



def leerArchivo(ruta):

    #El parámetro encoding permite leer los caracteres especiales del archivo
    archivo = open(ruta,"r", encoding="utf8")

    linea = []

    # Lee línea por línea del archivo y la guarda en una lista "linea" 
    # de 1 elemento

    for linea in archivo.readlines():
        
        # La lista campos contiene los datos de una persona
        # Los campos están separados por ";"
        campos = linea.replace("\n","").split(";")

        # Simplemente imprime de manera ordenada los datos de 1 persona
        imprimePersona(campos)


    archivo.close()

###############
##### MAIN ####
###############

#nombreArchivo = "personas.txt"
#crearArchivo(nombreArchivo)

ruta = str(pathlib.Path().absolute()) + "/" + "personas.txt"

leerArchivo(ruta)








