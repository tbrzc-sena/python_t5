#Escriba una función de Python que acepte una cadena y calcule el número de letras mayúsculas y minúsculas. 

def mayusAndMinus(cad):
    contMayus = 0
    contMinus = 0
    for i in cad:
        if i.isupper():
            contMayus+=1
        else:
            contMinus+=1
    return contMinus,contMayus

print(mayusAndMinus("MMMnn"))