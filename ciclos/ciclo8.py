def imprimir_patron(filas):
    contador = 1

    for i in range(1, filas + 1):
        for j in range(filas - i):
            print("-", end="")

        for k in range(1, i + 1):
            print(contador, end="_")
            contador += 1        
        print()

imprimir_patron(4)
