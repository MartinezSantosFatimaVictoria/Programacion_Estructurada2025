peliculas = []

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t...Oprima cualquier tecla para continuar...") 

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Películas ::.")
    nombre = input("Ingresa el nombre de la película: ").upper().strip()
    peliculas.append(nombre)
    print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::") 
    esperarTecla()

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Películas ::.")
    nombre = input("Ingresa el nombre de la película a borrar: ").upper().strip()
    if nombre in peliculas:
        cantidad = peliculas.count(nombre)
        for i in range(cantidad):
            peliculas.remove(nombre)
        print(f"\n\t::: ¡Se borraron {cantidad} película(s) con ese nombre! :::")
    else:
        print("\n\tNo se encontró esa película en el sistema.")
    esperarTecla() 

def mostrarPeliculas():
    borrarPantalla()
    if not peliculas:
        print("\n\tNo hay películas registradas.")
    else:
        print("\n\t.:: Listado de Películas ::.\n")
        for i, peli in enumerate(peliculas, start=1):
            print(f"\t{i}. {peli}")
    esperarTecla()

def limpiarPeliculas():
    borrarPantalla()
    print("\n\t.:: Limpiar o borrar TODAS las peliculas::.\n")
    resp=input("¿Deseas borrar todas las peliculas del sistema?(Si/No)").lower().strip()
    if resp=="si":
        peliculas.clear()

def buscarPeliculas():
    borrarPantalla()
    print("\n\t.::Buscar Pelicula::.\n")        
    pelicula_buscar=input("ingrese el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
         print("\n\t.:: Esta pelicula a buscar no existe en el sistema ::.\n")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"\n\t La pelicula {pelicula_buscar} se encontro en el casillero: {i+1}")
                encontro+=1
        print(f"\nTenemos {encontro} pelicula(s) con ese titulo")
        print("\n\t\t :::¡LA OPERACION SE REALIZO CON EXITO!:::")        
                
def ModificarPeliculas():
    borrarPantalla()
    print("\n\t.::Modificar Pelicula::.\n")        
    pelicula_buscar=input("ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
         print("\n\t.:: Esta pelicula a buscar no existe en el sistema ::.\n")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                resp=input("Desea actualizar la pelicula? (Si/No)").lower()
                if resp=="si":
                 peliculas[i]=input("\n Introduce el nuevo nombre de la pelicula: ").upper().strip()
                 encontro+=1   
                print("\n\t\t :::¡LA OPERACION SE REALIZO CON EXITO!:::")

        print(f"\nSe modifico {encontro}pelicula(s) con este titulo")

def menu():
    while True:
        borrarPantalla()
        print("\n\t=== MENÚ DE PELÍCULAS ===")
        print("\t1. Agregar película")
        print("\t2. Borrar pelicula")
        print("\t3. Mostrar películas")
        print("\t4. limpiar Pelicula")
        print("\t5. Buscar peliculas")
        print("\t6. Modificar peliculas")
        print("\t7. Salir")

        opcion = input("\n\tSelecciona una opción: ")

        if opcion == '1':
            agregarPeliculas()
        elif opcion == '2':
            borrarPeliculas()
        elif opcion == '3':
            mostrarPeliculas()
        elif opcion == '4':
            limpiarPeliculas()
        elif opcion == '5':
            buscarPeliculas()
        elif opcion == '6':
            ModificarPeliculas
        elif opcion ==7:    
            print("\n\tSaliendo del programa...")
            break
        else:
            print("\n\tOpción no válida.")
            esperarTecla()

# Ejecutar menú
menu()
