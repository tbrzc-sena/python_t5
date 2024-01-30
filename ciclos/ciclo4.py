# Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.
numeros = [float(input(f"Ingrese el número {i + 1}: ")) for i in range(10)]

suma = sum(numeros)
promedio = suma / len(numeros)

print("La suma de los números es:", suma)
print("El promedio de los números es:", promedio)

