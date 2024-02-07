#Escriba un programa Python para encontrar la lista de palabras que son más largas que n de una lista dada de palabras

def largoPalabra(n,palabras):
    lst = []
    for i in palabras:
        if len(i) > n:
            lst.append(i)
    return lst

lstPalabras = ['uno','dos','tre4s']

print(largoPalabra(4,lstPalabras))