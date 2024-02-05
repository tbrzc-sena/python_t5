#Escriba un programa Python para multiplicar todos los elementos de una lista.

lst = [8,5,4,2,2,3,0,7]
for i in range(len(lst)):
    if lst[i] == lst[-1]:
        break
    resultado = lst[i] * lst[i+1]
    print(resultado)
