#Solicitar notas de 0.0 a 5.0 a un estudiante y calcular promedio.  Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0.

#no se especifica una cantidad de notas :p
nota1 = float(input("Ingrese la primera nota (0.0 a 5.0): "))
nota2 = float(input("Ingrese la segunda nota (0.0 a 5.0): "))

promedio = (nota1 + nota2) / 2

if promedio >= 3.0:
    print("Aprobó con un promedio de", promedio)
else:
    print("No aprobó con un promedio de", promedio)

