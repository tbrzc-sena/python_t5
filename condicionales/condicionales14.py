#14. El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico se calcula con la fórmula:   
#Género femenino (1): número de pulsaciones = (220 - edad en años)/10   
#Género masculino (2): número de pulsaciones = (210 - edad en años)/10 
#Lea la edad y el género y muestre el número de pulsaciones.


def pulsaciones(edad,genero):
    if genero == 1:
        print((220 - edad)/10)
    else:
        print((210 - edad)/10)

edad = int(input("ingrese su edad: "))
print("digite 1 o 2 para seleccionar su genero: ",
      "1. femenino",
      "2. masculino")
genero = input()

pulsaciones(edad,genero)
