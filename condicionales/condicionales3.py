#Solicitar número al usuario y determinar si es negativo, positivo o cero.
numero = float(input("Ingrese un número: "))

if numero == 0:
    print("El número es cero.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es positivo.")

