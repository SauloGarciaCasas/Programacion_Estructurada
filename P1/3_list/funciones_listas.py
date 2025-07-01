"""

List (Array)
Son colecciones o conjunto de datos/valores bajo
un mismo nombre, para acceder a los valores se
hace con un índice numérico

Nota: sus valores si son modificables

La lista es una colecicón ordenada y
modificable. Permite miembros duplicados.

"""

#Funciones más comunes en las listas
import os
os.system("cls")

paises=["México","Brasil","España","Canadá"]

numeros=[23,12,100,34]


#Ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)

print(paises)
paises.sort()
print(paises)


#Añadir o ingresar o insertar elementos a una lista

#1er forma
print(paises)
paises.append("Honduras")

#2da forma
paises.insert(1,"Honduras")
print(paises)


#Eliminar o borrar o quitar elementos a una lista
#1er forma con el índice
paises.pop(1)
print(paises)

#2da forma con el valor
paises.remove("Honduras")
print(paises)


#Buscar un elemento dentro de la lista
#1er forma
resp = "Brasil" in paises
if resp:
    print("Si encontré el país")
else:
    print("No encontré el país")

#2da forma
#pais_buscar = input("Dame el pais a buscar: ")
for i in range (0,len(paises)):
    if paises[i]=="Brasil":
        print("Si encontré el país")
    else:
        print("No encontré el país")


#Cuantas veces aparece un elemento dentro de una lista
print(f"El numero 12 aparece: {numeros.count(12)} vez o veces")

numeros.append(12)
print(f"El numero 12 aparece: {numeros.count(12)} vez o veces")


#Identificar o conocer el índice de un valor
indice = paises.index("España")
print(indice)

paises.pop(indice)
print(paises)

#Recorrer los valores de la lista
#1er forma con los valores
for i in paises:
    print(i)

#2da forma con los indices
for i in range(0,len(paises)):
    print(f"El valor {i} es: {paises[i]}")

#Unir contenido de listas
print(paises)
print(numeros)
paises.extend(numeros)
print(paises)