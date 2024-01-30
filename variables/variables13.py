# Solicitar tiempo en segundos y transformar a horas y minutos. 
tiempo_segundos = int(input("Ingrese el tiempo en segundos: "))

horas = tiempo_segundos // 3600
minutos = (tiempo_segundos % 3600) // 60

print(f"El tiempo es de {horas} horas y {minutos} minutos.")

