"""
Estos son los ejercicios de la primera parte
del Máster en Python
"""

"""
#Ejercicio 1

Nombre="Diana" #Es un string
Edad=45 #Es un entero
print(f"Hola! Mi nombre es {Nombre} y tengo {Edad} años\n")

#Ejercicio 2

limite=int(input("¿Hasta qué número quieres llegar? "))

print(f"\nTe mostraremos los números pares del 1 al {limite}\n")

for i in range(1,limite+1):
    if (i%2 == 0):
        print(f"Este es un número par: {i}") 
else:
    print("\nSe acabaron los números")

"""
"""
# Ejercicio 3

limite = int(input("¿Hasta qué número desea calcular el cuadrado?:\n"))
contador = 1

while contador <= limite:
    print(f"Este es el cuadrado de {contador} : {contador ** 2}")
    contador += 1

"""
""""
#Ejercicios 4

print("Introduce 2 números")
a=int(input("a = "))
b=int(input("b = "))

print("\nLa suma de a + b = ", a+b)
print("La resta de a - b = ", a-b)
print("La multiplicación de a * b = ", a*b)
print("La división de a / b = ", a/b)
print("La división entera de a // b = ", a//b)
print("a elevado a la b = ", a**b)
print("a módulo b = ", a%b)
"""
"""
#Ejercicios 5

print("Introduce 2 números:")
a=int(input("a = "))
b=int(input("b = "))
contador=a
resultado=str(a)

if a < b:
    while contador < b:
        contador += 1
        resultado = resultado + ", " + str(contador)
        
    print(f"Estos son los números naturales entre {a} y {b} incluidos: {resultado}")
else:
    print(f"{a} es mayor o igual a {b}")
"""
"""
#Ejercicios 6

print("Estas son las tablas de mumtiplicar del 1 al 10:")

for tabla in range(1,11):
    
    print(f"\nEsta es la tabla del {tabla}")
    
    for i in range(1,11):
        print(f"{tabla} * {i} = {tabla * i}")

"""
"""
#Ejercicios 7

print("Introduce 2 números enteros:")
a=int(input("a = "))
b=int(input("b = "))

if a < b:
    print(f"\nTe mostraremos los números impares entre el {a} y el {b}\n")
    for i in range(a,b+1):
        if (i%2 == 1):
            print(f"Este es un número impar: {i}") 
else:
    print(f"{a} es mayor o igual a {b}")

"""
"""
#Ejercicios 8

a=int(input("Introduzca un número: "))
b=int(input("Ahora el porcentaje a calcular: "))

print(f"El {b} por ciento de {a} es: {a * b / 100}")
"""

"""
#Ejercicios 9

from random import randint

ganador = randint(1,10)
escoger = 0

while escoger != ganador:
    escoger=int(input("Introduce un número entero entre 1 y 10: "))
else:
    print("¡Felicidades! Eres el ganador")
"""
"""
#Ejercicio 10

aprobados = 0
reprobados = 0
alumnos = int(input("¿Cuántos alumnos son? "))

for i in range(1,alumnos + 1):
    nota = int(input(f"Introduzca la nota del alumno {i}: "))

    if nota >= 10:
        aprobados += 1
    else:
        reprobados += 1

print(f"{aprobados} alumnos han aprobado y {reprobados} alumnos han reprobado")
"""
#FUTTURO

from random import randint

flask = 0
django = 0
bigdata = 0
web = 0
escoger = 0

while escoger <=500:
    
    job = randint(1,4)

    if job == 1:
        flask += 1
    elif job == 2:
        django += 1
    elif job == 3:
        bigdata += 1
    elif job == 4:
        web += 1
    
    escoger += 1

print(f"flask: {flask}")
print(f"django: {django}")
print(f"bigdata: {bigdata}")
print(f"web: {web}")