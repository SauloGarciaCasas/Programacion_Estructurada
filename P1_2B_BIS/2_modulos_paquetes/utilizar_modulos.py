#1er forma de utilizar los modulos
import modulos

modulos.borrarPantalla

print(modulos.saludar("Saulo Garcia"))

#2da forma de utilizar los modulos

from modulos import saludar,borrarPantalla

#borrarPantalla()
print(saludar("Daniel Casas"))

#3ra forma de utilizar los modulos

nombre = input("Ingresa el nombre del contacto: ")
telefono = input("Ingresa el telefono del contacto: ")
nom,tel=modulos.solicitarDatos4(nombre,telefono)
print(f"\tNombre completo: {nom}\n\tTelefono: {tel}")
