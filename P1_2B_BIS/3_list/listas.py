#Ejemplo 1: Crear una lista de numeros e imprimir el código
import os
os.system("cls")

numeros=[1,2,3,4,5,6,7,8,9,10]

print(numeros)

for i in numeros:
    print(i)

for i in range(0,len(numeros)):
    print(numeros[i])

input("Oprima tecla ...")

#Ejemplo 2: Crear una lista de palabras y posteriormente buscar la coincidencio de una palabra
import os
os.system("cls")

palabras=["Si","Positivo","Afirmativo","Acuerdo","Adelante","Adelante"]
print(palabras)

palabra_buscar=input("Dame la palabra a buscar: ")

#1er forma
if palabra_buscar in palabras:
    print(f"Si encontré la palabra")
    print(f"La palabra {palabra_buscar} aparece: {palabras.count(palabra_buscar)} vez o veces")
else:
    print(f"No encontré la palabra")

#2da forma
encontro=False
for i in range (0,len(palabras)):
    if palabras[i]==palabra_buscar:
        encontro=True

if encontro:
    print(f"Si encontré la palabra")
    print(f"La palabra {palabra_buscar} aparece: {palabras.count(palabra_buscar)} vez o veces")
else:
    print("No encontré la palabra")

#3ra forma
encontro=False
for i in palabras:
    if i==palabra_buscar:
        encontro=True

if encontro:
    print(f"Si encontré la palabra")
    print(f"La palabra {palabra_buscar} aparece: {palabras.count(palabra_buscar)} vez o veces")
else:
    print("No encontré la palabra")

input("Oprima tecla ...")

#Ejemplo 3:Añador elementos a una lista
import os
os.system("cls")

numeros=[]

opcion=True

while opcion:
    num=float(input("Dame un numero entero o decimal: "))
    numeros.append(num)
    resp=input("Deseas agregar otro numero? ").lower()
    if resp=="si":
        opcion=True
    else:
        opcion=False

print (numeros)

input("Oprima tecla ...")

#Ejemplo 4: Crear una lista multidimensional que sea una agenda
import os
os.system("cls")

agenda=[
         ["Carlos","6181234567"],
         ["Alberto","6181594532"],
         ["Martin","6182563987"]
        ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

cadena=""
for r in range(0,3):
    for c in range(0,2):
        cadena+=f"{agenda[r][c]},"
    cadena+="\n"

print(cadena)