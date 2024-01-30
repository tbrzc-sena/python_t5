# Escriba un programa para mostrar la tabla de multiplicar de un entero dado.
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

