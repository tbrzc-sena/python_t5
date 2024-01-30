# Programa que permita calcular el 30%, el 60% y el 90% de cualquier número.
numero = int(input("Ingrese un número: "))

porcentaje_30 = 0.30
porcentaje_60 = 0.60
porcentaje_90 = 0.90

resultado_30 = numero * porcentaje_30
resultado_60 = numero * porcentaje_60
resultado_90 = numero * porcentaje_90

print(f"El 30% de {numero} es: {resultado_30}")
print(f"El 60% de {numero} es: {resultado_60}")
print(f"El 90% de {numero} es: {resultado_90}")

