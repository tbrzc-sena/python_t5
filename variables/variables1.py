#1. Programa que permita multiplicar 3 números.
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))


print("el resultado es: ",(lambda p1,p2,p3: p1*p2*p3)(n1,n2,n3))
