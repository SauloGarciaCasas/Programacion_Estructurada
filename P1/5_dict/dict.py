"""
dict.-
Es un tipo de datos que se utiliza para almacenar datos de diferente
tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos.
Es decir, es algo parecido como los objetos.

Tambien se conoce como un arreglo asociativo u objeto JSON

El diccionario es una colección ordenada y modificable. No hay miembbros duplicados.

"""
import os
os.system("cls")

#Lista
#paises=["Mexico","Brasil","Canada","España"]

#dict o objeto
pais_mexico={"Nombre":"Mexico","Capital":"CDMX","Poblacion":12000000,"Idioma":"Español","Status":True}

pais_brasil={"Nombre":"Brasil","Capital":"Brasilia","Poblacion":14000000,"Idioma":"Portugues","Status":True}

pais_canada={"Nombre":"Canada","Capital":"Otawa","Poblacion":9000000,"Idioma":["Ingles","Frances"],"Status":False}

alumnos1={"Nombre":"Daniel","Apellido_Paterno":"García","Apellido_Materno":"Casas","Carrera":"TI","Area":"Software Multiplataforma","Modalidad":"BIS","Matricula":"1234","Semestre":"2"}

print(alumnos1)

for i in alumnos1:
    print(f"{i}={alumnos1[i]}")

alumnos1["Telefono"]="6183245968"
for i in alumnos1:
    print(f"{i}={alumnos1[i]}")