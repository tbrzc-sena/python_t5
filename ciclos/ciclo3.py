# Escriba un programa para mostrar n términos de número natural y su suma (Fibonacci).
def fibonacci(n):
    a, b = 0, 1
    serie = []
    suma = 0
    for _ in range(n):
        serie.append(a)
        suma += a
        a, b = b, a + b
    return serie, suma

# Ejemplo de uso
n_terminos = 5
serie_fibonacci, suma_fibonacci = fibonacci(n_terminos)
print(f"Los primeros {n_terminos} términos de la serie Fibonacci son:", serie_fibonacci)
print("La suma de estos términos es:", suma_fibonacci)

