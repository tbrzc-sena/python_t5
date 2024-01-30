#El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado, como se muestra a continuación:
# Definir precios
precios_tamanos = {1: 15000, 2: 24000, 3: 36000}#aclaracion es un diccionario, clave valor. Se llama por la clave y retorna el valor 
precio_ingrediente_adicional = 4000

# Solicitar al empleado los datos de la pizza
tamaño_pizza = int(input("Ingrese el tamaño de la pizza (1, 2 o 3): "))
ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales: "))

# Calcular el precio total de la pizza
precio_base = precios_tamanos[tamaño_pizza] #forma de acceder a un dicccionario tambien es posible con mi_diccionario["key1"]
precio_total = precio_base + (ingredientes_adicionales * precio_ingrediente_adicional)

# Mostrar el precio al cliente
print(f'El precio a pagar por la pizza es: ${precio_total}')

