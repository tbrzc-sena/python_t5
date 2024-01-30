# Escriba un programa para mostrar el patrón como triángulo con un asterisco. El patrón como:
a = "×"
c = 1

for i in range(1,10):
    if i < 5:
        print(a)
        a += '×'
        c +=1
    else:
        if c == 5:

            print(a)
            c-=1
        else:
            a = a[:-1]
            print(a)
            c-=1
