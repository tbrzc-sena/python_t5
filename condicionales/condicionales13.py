#Un reporte de salud muestra una tabla diferente del índice de masa corporal IMC de una persona que se calcula con la fórmula IMC=P/(E*E) en donde P es el peso en Kg. y E es la estatura en metros. Lea un valor de P y de E, calcule el IMC y muestre su estado según la siguiente tabla:

peso = float(input("digite su peso en kg: "))
estatura = float(input("digite su estatura en metros: "))

imc = lambda peso_kg,estatura_m:  peso_kg / (estatura_m * estatura_m)

IMC = imc(peso,estatura/100)

if IMC < 18.5:
    print("Desnutrido")
elif 18.5 <= IMC < 25:
    print("Normal")
elif 25 <= IMC <30:
    print("Sobrepeso")
elif 30 <= IMC < 35:
    print("Obesidad grado 1")
elif 35 <= IMC < 40:
    print("Obesidad grado 2")
else:
    print("Obesidad grado 3")
