#chatgpt lo hizo
cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
precio_unitario_original = float(input("Ingrese el precio unitario original: "))

if cantidad_articulos <= 5:
    total_pagar = cantidad_articulos * precio_unitario_original
elif 5 < cantidad_articulos < 10:
    descuento = 0.05  
    total_pagar = cantidad_articulos * (1 - descuento) * precio_unitario_original #????
else:
    descuento = 0.08  
    total_pagar = cantidad_articulos * (1 - descuento) * precio_unitario_original


print("El total a pagar es: ${:.2f}".format(total_pagar))

