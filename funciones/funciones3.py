#Escriba una función de Python para sumar todos los números de una lista. Lista de muestras: (8, 2, 3, 0, 7)Resultado esperado: 20.

def sumAllNumsList(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
lst = [8,2,3,0,7]
print(sumAllNumsList(lst))