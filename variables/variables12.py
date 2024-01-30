# Calcular la hipotenusa con el Teorema de Pitágoras.
import math

cateto1 = float(input("Ingrese la longitud del primer cateto: "))
cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print("La longitud de la hipotenusa es:", hipotenusa)

