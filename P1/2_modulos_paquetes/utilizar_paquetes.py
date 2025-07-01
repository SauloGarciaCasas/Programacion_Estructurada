from paquete1 import modulos

modulos.borrarPantalla()
print(modulos.saludar("Daniel Casas"))

nombre, telefono = modulos.solicitarDatos2()
print(f"\n\t.:: Agenda Telefónica ::.\n\t\tNombre: {nombre}\n\t\tTelefono: {telefono}")
modulos.espereTecla()