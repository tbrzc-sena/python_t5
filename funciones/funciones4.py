#Escriba una función de Python para multiplicar todos los números de una lista. Lista de muestra: (8, 2, 3, -1, 7)Resultado esperado: -336

def multAllNumsList(lst):
    sum = lst[0]
    for i in range(1,len(lst)):
        sum *=lst[i]
    return sum
lst = [8,2,3,-1,7]
print(multAllNumsList(lst))