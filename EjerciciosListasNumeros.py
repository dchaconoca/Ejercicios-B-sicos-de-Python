"""
Estos son los ejercicios de la asegund parte
del Máster en Python
"""

"""
#Ejercicio 1 
Manejo de listas de números
"""

def crearLista():
    i = 0
    numeros = []
    cantidad = int(input("¿Cuántos números desea introducir? "))

    while i < cantidad:
        numeros.insert(i,int(input("Introduzca un número: ")))
        i += 1
    
    return numeros

def ordenarLista(lista):

    ordenada = []
    i = 0
    
    while i < len(lista):

        minimo = min(lista)
        ordenada.append(minimo)
        lista.remove(minimo)

    return ordenada

def buscarDato(dato, lista):
    """
    Versión 1
    return dato in lista
    """

    if dato in lista:
        posicion = lista.index(dato)

        print(f"El número {buscar} se encuentra en la lista en la posición {posicion}")
    else:
        print(f"El número {buscar} NO se encuentra en la lista")

###############
##### MAIN ####
###############

listaNumeros = crearLista()

print("\nEsta es la lista de números introducidos:\n")

print(listaNumeros,"\n")

print(f"Esta lista tiene {len(listaNumeros)} elementos\n")

#listaOrdenada = ordenarLista(listaNumeros)

print("\nEsta es la lista ordenada:\n")

listaNumeros.sort()

print(listaNumeros, "\n")

buscar = int(input("Introduzca el número que quiere buscar: "))

buscarDato(buscar, listaNumeros)
  

