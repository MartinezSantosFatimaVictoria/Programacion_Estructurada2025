pelicula = []
def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

#Diccionaro u objeto para almacenar los siguientes atributos de las peliculas: nombre, categoria, clasificacion, genero, idioma

def  crearPeliculas() :
    borrarPantalla()
    print ("\n\t•.:: •Agregar• Películas•::.\n")
    pelicula.update({"nombre": input("Ingresa el nombre:"). upper().strip()})
    pelicula.update({"categoria": input ("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion": input("Ingresa la clasificación: -").upper(). strip()})
    pelicula.update({"genero": input("Ingresa-el genero: "). upper(). strip()})
    pelicula.update({"idioma": input("Ingresa el idiomas.").upper().strip()})
    print("\n\t\t.:::LA OPERACION SE REALIZO CON EXİTO!:::")
   

    def mostrarPeliculas():
        borrarPantalla()
        if not pelicula:
            print("\n\tNo hay películas registradas.")
        else:
            print("\n\t.:: Listado de Películas ::.\n")
    for i, peli in enumerate(pelicula, start=1):
            print(f"\t{i}. {peli}")
    esperarTecla()

def borrarPeliculas():
     borrarPantalla()
     print("\n\t .:: Borrar o quitar la pelicula ::. \n")
     if len(pelicula)>0:
          resp=input("Deseas borrar o quitar la pelicula? (SI/NO)").lower().strip()
          if resp=="si":
               pelicula.clear()
     else:
          print("\n\t .:: No hay peliculas en el sistema ::.")

def agregarCaracteristicaPeliculas():
     borrarPantalla()
     print("\n\t .:: Agregar una caracteristica de peliculas ::. \n")
     atributo=input("ingresa el nombre de la nueva caracteristica que deseas agregar: ").lower().strip()
     valor_atributo=input("Ingresa el valor de la nueva caracteristica que agregar: ").upper().strip()
     pelicula.update({atributo:valor_atributo})
     print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")


def modificarCaracteristicaPeliculas():
     borrarPantalla()
     print("\n\t.::Modificar una característica de Película::.\n")
if len(pelicula)>0:
        for i in pelicula:
            print(f"{i} : {pelicula[i]}")
            resp=input(f"\n\t ¿Deseas modificar el valor de la caracteristica {i}?(SI/NO)").lower().strip()
            if resp=="si":
                valor=input(f"\n\t Ingresa el nuevo valor de la caracteristica {i}").upper().strip()
                pelicula[i]=valor
                print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::")
                esperarTecla()
else:
        print("\n\t.::No hay peliculas en el sistema::.")
        borrarPantalla()

def borrarCaracteristicaPeliculas():
           borrarPantalla()
           print("\n\t.::Modificar una característica de Película::.\n")
if len(pelicula)>0:
     print(f"{i} : {pelicula[i]}")
     print("\n\t Valores actuales:{i}")
     resp=input(f"\n\t ¿Deseas borrar alguna caracteristica {i}?(SI/NO)").lower().strip()
     if resp=="si":
          borrar=input(f"\n\t ingresa la caracteristica que deseas borrar o quitar {i}").upper().strip()
          pelicula[i]=borrar
          print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::")
          esperarTecla()
else:
     print("\n\t.::No hay peliculas en el sistema::.")         
     borrarPantalla()



