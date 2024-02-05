#Escriba una función de Python para encontrar el máximo de tres números.
def mayorDeTres(n1,n2,n3):
    return max(n1,max(n2,n3))

print(mayorDeTres(7,1,2))