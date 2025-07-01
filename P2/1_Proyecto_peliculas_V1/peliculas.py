# Funciones para gestionar películas

peliculas = []

def agregar():
    nombre = input("Nombre de la película a agregar: ")
    peliculas.append(nombre)
    input("Película agregada. Oprima cualquier tecla para continuar ...")

def eliminar():
    nombre = input("Nombre de la película a eliminar: ")
    
    if nombre in peliculas:
        resp = input("Deseas eliminar esta película? Si/No: ").lower
        if resp == "si":
            peliculas.remove(nombre)
            print(f"Se borró la película: {nombre}")
            input("Oprima cualquier tecla para continuar ...")
    else:
        input("Esta película no existe. Oprima cualquier tecla para continuar ...")

def actualizar():
    viejo = input("Nombre actual de la película: ")
    if viejo in peliculas:
        nuevo = input("Nuevo nombre: ")
        idx = peliculas.index(viejo)
        peliculas[idx] = nuevo
        input("Película actualizada. Oprima cualquier tecla para continuar ...")
    else:
        input("Esta película no existe. Oprima cualquier tecla para continuar ...")


def consultar():
    return peliculas

def buscar(nombre):
    return nombre in peliculas

def vaciar():
    peliculas.clear()

def borrarPantalla():
    import os
    os.system("cls")