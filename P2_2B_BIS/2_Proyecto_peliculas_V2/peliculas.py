# Funciones para gestionar películas

#peliculas = {"Nombre":"","Categoría":"","Clasificación":"","Género":"","Idioma":""}

pelicula = {}

def borrarPantalla():
    import os
    os.system("cls")

def crear():
    print("\n\t.:: Alta de Peliculas ::.\n")
    pelicula.update({"nombre": input ("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria":input ("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion":input ("Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"genero":input ("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input ("Ingresa el idioma: ").upper().strip()})
    input("\n\t\t ::: LA OPERACION SE REALIZO CON EXITO ::::")

def mostrar():
    print("\n\t.:: Mostrar TODAS la Peliculas :::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t {(i)}:{pelicula[i]}")
            input("Oprima cualquier tecla para continuar ...")
    else:
        print("\t .:: No hay peliculas en el sistema ::.")
        input("Oprima cualquier tecla para continuar ...")

def borrar():
    print("\n\t.:: Borrar TODAS la Peliculas :::.\n")
    resp = input("Deseas quitar todas las peliculas? Si/No: ").lower()
    if resp == "si":
        pelicula.clear()
        input("\n\t\t ::: LA OPERACION SE REALIZO CON EXITO ::::")
        input("Oprima cualquier tecla para continuar ...")

def agregarcar():
    print("\n\t.:: Agregar Caracteristica a Películas ::.\n")
    atributo=input("Ingresa la nueva caracteristica de la película: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica de la de la película: ").upper().strip()
    pelicula[atributo]=valor
    print("\n\t\t ::: LA OPERACION SE REALIZO  CON EXITO! :::")
    input("Oprima cualquier tecla para continuar ...")

def modificarcar():
    print("\n\t.:: Modificar Característica de Películas ::.\n")
    atributo = input("Ingresa el nombre de la característica a modificar: ").lower().strip()
    if atributo in pelicula:
        nuevo_valor = input(f"Ingrese el nuevo valor para '{atributo}': ").upper().strip()
        pelicula[atributo] = nuevo_valor
        print("\n\t\t ::: LA OPERACIÓN SE REALIZÓ CON ÉXITO :::")
    else:
        print(f"\n\tLa característica '{atributo}' no existe.")
    input("Oprima cualquier tecla para continuar ...")

    if len(pelicula) == 0:
        print("\tNo hay características que modificar.")
        input("Oprima cualquier tecla para continuar ...")
        return

def borrarcar():
    print("\n\t.:: Borrar Característica de Películas ::.\n")
    atributo = input("Ingresa el nombre de la característica a eliminar: ").lower().strip()
    if atributo in pelicula:
        del pelicula[atributo]
        print(f"\n\t\t ::: LA CARACTERÍSTICA '{atributo}' SE ELIMINÓ CON ÉXITO :::")
    else:
        print(f"\n\tLa característica '{atributo}' no existe.")
    input("Oprima cualquier tecla para continuar ...")

    if len(pelicula) == 0:
        print("\tNo hay características que eliminar.")
        input("Oprima cualquier tecla para continuar ...")
        return