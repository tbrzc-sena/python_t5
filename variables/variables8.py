# Programa que permita ingresar 5 números y calcular el promedio
suma = 0

for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    suma += numero

promedio = suma / 5

print("El promedio de los números es:", promedio)

