#Escriba un programa para calcular las áreas de las figuras geométricas utilizando una función para cada área. 
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


#para usar cada una de las funciones hacer el llamado (obviamente)