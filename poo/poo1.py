#Escriba una clase que represente un vehículo con métodos y atributos. Dentro atributos cree uno llamado “placa” y en los métodos cree uno que permita determinar de acuerdo con el día, si el vehículo tiene restricción por pico y placa o no, en la ciudad de Bogotá. 
import datetime
class Vehiculo:
    
    # pass crea un constructor vacio
    def __init__(self,placa) -> None: #el self es una variable que representa la instancia de la clase, y deberá estar siempre ahí. al igual que el init que reprensenta el constructor
        self.placa = placa

    def hasRestriccion(self):
        dia = int(datetime.datetime.now().strftime("%w"))
        ultimoDigitoPlaca = int(self.placa[-1])
        if dia % 2 != 0 and 1<ultimoDigitoPlaca<5:
            print("Su vehiculo puede circular")
        else:
            print("Su vehiculo NO puede circular")

mi_vehiculo = Vehiculo('AAA332')
mi_vehiculo.hasRestriccion()
