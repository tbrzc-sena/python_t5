#Escriba una función de Python que tome un número como parámetro y verifique que el número sea primo o no. Un número primo (o primo) es un número natural mayor que 1 y que no tiene divisores positivos aparte de 1 y sí mismo.

def isPrimo(n):
    return n % 2 == 0

print(isPrimo(5))