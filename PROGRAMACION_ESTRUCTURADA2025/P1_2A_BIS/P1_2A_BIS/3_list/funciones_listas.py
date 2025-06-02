'''
list(Array)

son colecciones o conjunto de datos/valores bajo un mismo nombre, 
para acceder a los valores se hace con indice numerico

Nota: sus valores si son modificables

la lista es una coleccion ordenada y modificable. Permite miembros duplicados.
'''

import os
os.system("clean")

#Funciones mas comunes en las listas

paises=["Mexico", "España","Brasil","Canada"]

numeros=[23,45,8,24]

varios=["hola",3.1416,33,True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)

#Recorrer la lista
#1er forma

for i in paises:
    print(i)

#2da forma
for i in range(0,len(paises)):
    print(paises[i])

#ordenar elementos de una lista
paises.sort() 
print(paises)

numeros.sort()
print(numeros)

#Dar vuelta a una lista
paises.reverse()
print(paises)

varios.reverse()
print(varios)

#Agregar, insertar, Añadir un elemento a una lista
#1ra forma
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar,borrar, suprimir, un elemento de la lista 
#1er forma
paises.pop(4)
print(paises)

#2da forma
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista
resp="Brasil" in paises
print(resp)

#contar el numero de veces que aparece un elemento dentro de una lista
cuantos=numeros.count(23)
print(cuantos)

#conocer la posicion o indice en la que se encuentra un elemento de la lista
print(paises)
posicion=paises.index ("Canada")

print(f"El valor de Canada lo encontro en la posicion:{posicion}")

#unir el contenido de una lista dentro de otra lista

print(numeros)
numeros2=[100,200]
print(numeros2)

#crear a partir de las listas de numeros 1 y 2 
#una reesultante y mostrar el contenido ordenado desendentemente
numeros.extend(numeros2)
print(numeros)

numeros.sort()
print(numeros)
numeros.reverse()
print(numeros )
