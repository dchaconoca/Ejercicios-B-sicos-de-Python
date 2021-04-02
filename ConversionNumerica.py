"""
##################################
EJERCICIOS CONVIRTIENDO NÚMEROS
EN DIFERENTES BASES DE 2 A 16
##################################
"""

from time import time

def esLetra(res):
    
    letras = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F']

    try:
        res = str(res).upper()

        if res in letras:
            return letras.index(res)
        else:
            return letras[int(res)]
    
    except:
        print("Fuera de rango")
    

"""
Función que devuelve la representación de un número entero positivo
en el sistema BASE:

Un número en otra base diferente de 10 está formado por la concatenación 
(string) de los restos de dividir sucesivamente un número (entero del 
cociente) hasta que el cociente sea menor que la base
"""

def decimalABase(n, base):
    try:
        result = ""
        if n < 0:
            return "El número no es válido"
        else:
            while n >= base:
                resto = (n % base)
                n = int(n / base)
                if resto >= 10:
                    resto = esLetra(resto)

                result = str(resto) + result

            if n >= 10:
                n = esLetra(n)

            return str(n) + result
           
    except:
        return "No es un número"

"""
La misma función pero recursiva
En principio es más rápida
""" 
def decimalABaseRecur(n, base):
    try:
        if n < 0:
            return "El número no es válido"
        else:
            if n < base:
                if n >= 10:
                    n = esLetra(n)
                return str(n)
            else:
                resto = (n % base)
                n = int(n / base)

                if resto >= 10:
                    resto = esLetra(resto)

                return decimalABase(n, base) + str(resto)
    except:
        return "No es un número"

"""
Función que devuelve el número decimal de un número en base "base" dado:
"""
def baseADecimal(n, base):
    n = str(n)
    i = len(n)-1
    result = 0
    for c in n:
        num = int(esLetra(c))
        result = result + (num * (base**i))
        i+=-1
    
    return result

def main():

    continuar = "S"

    while continuar.upper() == "S":
        n = int(input("\nIntroduzca el número entero que desea convertir: "))
        base = int(input("Introduzca la base (2 a 16): "))

        print(f"\nResultado del entero {n} en base {base} y su tiempo de ejecución con un while")
        start_time = time()
        res = decimalABase(n, base)
        print(f"El resultado es: {res} ")
        elapsed_time = time() - start_time
        print("Elapsed time: %.10f seconds." % elapsed_time + "\n")

        print(f"Resultado del entero {n} en base {base} y su tiempo de ejecución con función recursiva")
        start_time = time()
        res = decimalABaseRecur(n, base)
        print(f"El resultado es: {res} ")
        elapsed_time = time() - start_time
        print("Elapsed time: %.10f seconds." % elapsed_time  + "\n")

        print(f"Y ahora el resultado {res} en base {base} lo transformamos a base decimal ")
        
        dec = baseADecimal(res, base)

        print(f"El resultado es: {dec} \n")

        continuar = input("¿Desea continuar con otro número? S/N: ")

    
if __name__ == '__main__': main()


