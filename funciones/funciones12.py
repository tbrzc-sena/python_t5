#Escriba una función de Python que compruebe si una cadena pasada es palíndromo o no. Una palabra o frase que es palíndromo se lee igual de izquierda a derecha que de derecha a izquierda. Por ejemplo: Ana, Anita lava la tina.

def palindromo(string):
    if string[::-1].lower() == string:
        return True
    else:
        return False

print(palindromo("anaa"))