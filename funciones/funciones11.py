#Escriba un programa Python para imprimir los números pares de una lista determinada.
def paresLst(lst):
    lstUnica = []
    for i in lst:
        if i % 2 == 0:
            lstUnica.append(i)
    return lstUnica
lst = [8,5,4,2,2,3,0,7]
print(paresLst(lst))