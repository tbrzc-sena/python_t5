# Solicitar al usuario una distancia en metros y transformar a km., cm. o mm.
distancia_metros = float(input("Ingrese la distancia en metros: "))

distancia_km = distancia_metros / 1000
distancia_cm = distancia_metros * 100
distancia_mm = distancia_metros * 1000

print(f"La distancia es de {distancia_km} km, {distancia_cm} cm y {distancia_mm} mm.")

