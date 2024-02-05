#Escriba una función de Python que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista. 
def ElementosUnicos(lst):
    lstUnica = []
    for i in lst:
        if i not in lstUnica:
            lstUnica.append(i)
    return lstUnica
lst = [8,4,2,2,3,0,7]
print(ElementosUnicos(lst))