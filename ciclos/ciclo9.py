#Escriba un programa para calcular el factorial de un número dado.
def factorial(num):
    alm = num
    for i in range(1,num):
       num *= i 
    print(f'El factorial de {alm} es: {num}')

factorial(5)
