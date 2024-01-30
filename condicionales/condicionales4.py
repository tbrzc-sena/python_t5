#Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado.
numero1 = float(input("Ingrese el primer número: "))#4
numero2 = float(input("Ingrese el segundo número: "))#1

if numero1 > numero2:
    print("El número mayor es:", numero1)
    print("El número menor es:", numero2)
elif numero2 > numero1:
    print("El número mayor es:", numero2)
    print("El número menor es:", numero1)

