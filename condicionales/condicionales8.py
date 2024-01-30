#Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente.

numeros = []

for i in range(3):
    numero = float(input("Ingrese el número {}: ".format(i + 1)))
    numeros.append(numero)

ascendente = sorted(numeros)
descendente = sorted(numeros, reverse=True)

print("Números en orden ascendente:", ascendente)
print("Números en orden descendente:", descendente)

