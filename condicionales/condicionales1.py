#Solicitar número al usuario y determinar si es par, impar o es cero.
numero = int(input("Ingrese un número: "))

if numero == 0:
    print("El número es cero.")
elif numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

