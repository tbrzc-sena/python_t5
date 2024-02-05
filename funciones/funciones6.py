#Escriba una función de Python para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento.
def factorial(num):
    alm = num
    for i in range(1,num):
       num *= i 
    print(f'El factorial de {alm} es: {num}')

factorial(5)
