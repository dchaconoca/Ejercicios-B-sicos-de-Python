"""
Estos son los ejercicios de la asegund parte
del Máster en Python
"""

"""
#Ejercicio 2
Manejo de cadenas de caracteres
"""

def introducirCadenaCaracteres():

    frase = ""

    while frase == "":
        frase = input("Introduzca una frase: ")

        if frase == "":
            print("Debe introducir una frase")

    return frase

def formatearCadena(cadena):

    mayusculas = ""
    minusculas = ""
    capitales = ""
    palabrar = []

    mayusculas = cadena.upper()
    minusculas = cadena.lower()
    capitales = cadena.title()
    palabras = cadena.split()
    numCarcteres = len(cadena)

    print("Esta es la frase en mayúsculas:\t", mayusculas)
    print("Esta es la frase en minúsculas:\t", minusculas)
    print("Esta es la frase en capitales:\t", capitales)
    print("Esta es la lista de palabras de la frase:\t", palabras)

    return palabras

def ordenarListaPalabras(lista):
    ordenada = []
    i = 0
    
    while i < len(lista):

        minimo = min(lista)
        ordenada.append(minimo)
        lista.remove(minimo)

    return ordenada


###############
##### MAIN ####
###############

cadena = introducirCadenaCaracteres()

#Deja 50 espacios a la izquierda antes de escribir el valor de cadena
print(f"\nEsta es la frase introducida: {cadena:>50}")

print(f"\nY tiene {len(cadena)} caracteres")

palabras = formatearCadena(cadena)

palabras.sort()

print("\nEstas son las palabras de la frase ordenadas alfabéticamente:\t", palabras)
