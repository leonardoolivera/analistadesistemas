import math

a = float(input("Digite o valor de a"))
b = float(input("Digite o valor de b"))
c = float(input("Digite o valor de c"))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação de 2º grau não possui raízes reais!  :(")   
elif delta == 0:
    x = -b / (2*a)
    print("Existe apenas uma solução para o problema. 'X' é igual à :",x)
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Existem duas soluções para o problema. X1 é igual a:",x1, "e X2 é igual a: ",x2)


