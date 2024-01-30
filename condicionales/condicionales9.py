#Programa que permita a un usuario tomar una decisión del tipo de pago a usar. Si la cuenta es menor a $150000 pago en efectivo. Si no, si es de $150000 hasta $300000 pago con el celular (dinero electrónico). Si es mayor a $300000 hasta $600000, pago con la tarjeta de débito. Caso contrario, pago con la tarjeta de crédito.
monto_cuenta = float(input("Ingrese el monto de la cuenta: "))

if monto_cuenta < 150000:
    print("Pago en efectivo.")
elif 150000 <= monto_cuenta <= 300000:
    print("Pago con celular (dinero electrónico).")
elif 300000 < monto_cuenta <= 600000:
    print("Pago con tarjeta de débito.")
else:
    print("Pago con tarjeta de crédito.")

