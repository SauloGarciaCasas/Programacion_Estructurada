"""
Version 1
Crear un programa que calcule e imprima cualquier tabla de multiplicar

Requisitos:
1.- Sin estructuras de control
2.- Sin funciones

"""

num=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
mult=num*1
print(f"{num}x1={mult}")

mult=num*2
print(f"{num}x2={mult}")

mult=num*3
print(f"{num}x3={mult}")

mult=num*4
print(f"{num}x4={mult}")

mult=num*5
print(f"{num}x5={mult}")

mult=num*6
print(f"{num}x6={mult}")

mult=num*7
print(f"{num}x7={mult}")

mult=num*8
print(f"{num}x8={mult}")

mult=num*9
print(f"{num}x9={mult}")

mult=num*10
print(f"{num}x10={mult}")

mult=num*11
print(f"{num}x11={mult}")

mult=num*12
print(f"{num}x12={mult}")

"""
Version 2

Crear un programa que calcule e imprima cualquier tabla de multiplicar

Requisitos:
1.- Sin funciones

"""

num=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
for i in range(1,11):
    multi=num*i
    print(f"{num} x {i} = {multi}")

num=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
i=1
while i <= 12:
    multi=num*i
    print(f"{num} x {i} = {multi}")
    i+=1

"""
Version 3

Crear un programa que calcule e imprima cualquier tabla de multiplicar

Con funciones que regrese valor y utilice parametros

"""

def tabla(numero):
    num=numero
    respuesta=""

    for i in range(1,11):
        multi=num*i
        respuesta+=f"\t{num} x {i} = {multi}\n"
    return respuesta

numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
print(f"Tabla de multiplicar del {numero}")
resultado=tabla(numero)
print(f"{resultado}")