#Ejemplo 1 crear una lista de numeros e imprimir el contenido
numeros=[8,30,5,25,238]
print(numeros)

lista="["
for i in numeros:
    lista+f"{i},"
    print(f"{lista}")

#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
palabras=["pilas","hola","blackie","profesor"]
palabra_buscar=input("Dame la palabra a buscar:")


if palabra_buscar in palabras:
    print("Si se encontro la palabra en la lista")
else:
    print("No se encontro la palabra en la lista")    

#2da forma
encontro=False
for i in palabras:
    if i==palabra_buscar:
       encontro=True
if encontro:      
       print("Si se encontro la palabra en la lista")
else:
       print("No se encontro la palabra en la lista")

     



#Ejemplo 3 Añadir  elementos a la lista
numeros.append(78)
print(numeros)

palabras.append("Brownies")
print(palabras)

#Ejemplo 4 crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[["Theodora","618-324-7698"],["Vannesa","618-874-2343"],["Karen","618-992-1416"]]
