'''
1. Cargar una matriz con datos de personas
Crear una matriz de 4 filas y 3 columnas. Cada fila representa una persona y cada columna representa:
nombre, edad y ciudad. Pedir al usuario que cargue los datos y mostrarlos con formato de tabla.

2. Contar cuántas personas tienen más de 30 años
Con una matriz previamente cargada con nombre, edad y ciudad, recorrer la matriz y contar cuántas
personas tienen más de 30 años. Mostrar el total.
'''

import constantes



personas = [[0] * constantes.COLUMNAS for persona in range(constantes.FILAS)]

print("Ingrese los datos de las personas")

for i in range(constantes.FILAS):
    print(f"Persona {i + 1}")
    personas[i][constantes.INDICE_NOMBBRE] = input("Nombre: ")
    personas[i][constantes.INDICE_EDAD] = int(input("Edad: "))
    personas[i][constantes.INDICE_CIUDAD] = input("ciudad: ")

print("----------------------------------------")
print("Muestra de datos")
print("----------------------------------------")

for fila in personas:
    print(f"{fila[0]} \t\t {fila[1]} \t\t {fila[2]}")

mayores_30 = 0

for i in range(constantes.FILAS):
    edad = personas[i][constantes.INDICE_EDAD]
    if edad > 30:
        mayores_30 += 1

print(f"La cantidad de persoonas con mas de 30 años es: {mayores_30}")
