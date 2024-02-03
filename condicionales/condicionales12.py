cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
precio_unitario_original = float(input("Ingrese el precio unitario original: "))

if cantidad_articulos <= 5:
    total_pagar = cantidad_articulos * precio_unitario_original
elif 5 < cantidad_articulos < 10:
    descuento = 0.05  
    total_pagar = (precio_unitario_original + (precio_unitario_original * descuento)) * cantidad_articulos 
else:
    descuento = 0.08  
    total_pagar = (precio_unitario_original + (precio_unitario_original * descuento)) * cantidad_articulos

print("El total a pagar es: ${}".format(total_pagar))

