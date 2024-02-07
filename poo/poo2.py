#Escriba una clase de Python llamada Rectangle construida por una longitud y anchura y un método que calculará el área de un rectángulo.

class Rectangle:
    
    # pass crea un constructor vacio
    def __init__(self,longitud,anchura) -> None: #el self es una variable que representa la instancia de la clase, y deberá estar siempre ahí. al igual que el init que reprensenta el constructor
        self.longitud = longitud
        self.anchura = anchura

    def areaRectangulo(self):
        print(self.anchura * self.longitud)

mi_vehiculo = Rectangle(2,3)
mi_vehiculo.areaRectangulo()
