"""
Es un tipo de datos para tener una colección de valores pero no tiene ni indice ni orden.

Sets es una colección desordenada, inmutable y no indexada.
No hay miembros duplicados.

"""
import os
os.system("cls")

personas={"Ramiro","Coche","Lupe"}
print(personas)
personas.add("Peje")
print(personas)
personas.pop()
print(personas)
personas.clear()
print(personas)

varios={3.12,3,True,"Hola"}
print(varios)

#Ejemplo: Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en la pantalla los email sin duplicados

opc="si"
email=[]
while opc=="si":
    email.append(input("Dame el email: "))
    print(email)
    opc=input("Deseas solicitar otro email? si/no").lower()

print(email)
set1=set(email)
print(set1)
email=list(set1)
print(email)