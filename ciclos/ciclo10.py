#Escriba un programa para mostrar un patrón como Z con asteriscos.
def z():
   contador = 9
   for i in range(9):
      print("*",end="")
   print("*")
   for i in range(9):
      for j in range(contador,1,-1):
         print(" ",end="")
      print("*")
      contador-= 1
   for i in range(9):
       print("*",end="")
z()

