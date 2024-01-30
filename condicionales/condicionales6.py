#Crear un programa con un menú de opciones, que permita calcular las áreas de figuras geométricas (cuadrado, rectángulo, triángulo, círculo, rombo y trapecio).
import math

def area_cuadrado(lado):
    return lado * lado

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * radio**2

def area_paralelogramo(base, altura):
    return base * altura

def area_triangulo_equilatero(lado):
    return (lado**2 * math.sqrt(3)) / 4

#def area_triangulo_rectangulo(base, altura):
#    return (base * altura) / 2
def area_poligono_regular(longitud_apotema, perimetro):
    return (longitud_apotema * perimetro) / 2 

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) / 2) * altura

while True:
    print("\nMenú de opciones:")
    print("1. Calcular área de rectángulo")
    print("2. Calcular área de cuadrado")
    print("3. Calcular área de un paralelogramo")
    print("4. Calcular área de un rombo")
    print("5. Calcular área de trapecio")
    print("6. Calcular área de triángulo")
    print("7. Calcular área de triángulo equilatero")
    print("8. Calcular área de triángulo rectangulo")
    print("9. Calcular área de un poligono regular")
    print("10. Calcular área de círculo") 
    print("0. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 0:
        break
    elif opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print("El área del rectángulo es:", area_rectangulo(base, altura)) 
    elif opcion == 2:
        lado = float(input("Ingrese el lado del cuadrado: "))
        print("El área del cuadrado es:", area_cuadrado(lado))
    elif opcion == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es:", area_triangulo(base, altura))
    elif opcion == 4:
        base = float(input("Ingrese la base del paralelogramo: "))
        altura = float(input("Ingrese la altura del paralelogramo: "))
        print("El área del paralelogramo es:", area_paralelogramo(base, altura))
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es:", area_circulo(radio))
    elif opcion == 5:
        base_mayor = float(input("Ingrese la base mayor del trapecio: "))
        base_menor = float(input("Ingrese la base menor del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        print("El área del trapecio es:", area_trapecio(base_mayor, base_menor, altura))
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

