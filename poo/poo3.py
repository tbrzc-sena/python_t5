#Escriba una clase de Python llamada Circle construida por un radio y dos métodos que calcularán el área y el perímetro de un círculo.
import math
class Circle:
    
    # pass crea un constructor vacio
    def __init__(self,radio) -> None: #el self es una variable que representa la instancia de la clase, y deberá estar siempre ahí. al igual que el init que reprensenta el constructor
        self.radio = radio

    def area(self):
        print(math.pi * (self.radio **2))

    def perímetro(self):
        print(math.pi * 2 * self.radio)

circulo = Circle(3)
circulo.perímetro()
circulo.area()
