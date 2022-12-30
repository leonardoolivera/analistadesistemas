#Um número palindrômico lê o mesmo nos dois sentidos. O maior palíndromo feito a partir do produto de dois números de 2 dígitos é 9009 = 91 × 99.

#Encontre o maior palíndromo feito a partir do produto de dois números de 3 dígitos.

numero1 = 999
resultado = ()
maior = 0

for i in range(9,1000):
    numero1 -= 1
    for j in range(9,1000):
        resultado = (str(numero1 * j))
        if resultado == resultado[::-1]:
            resultado = int(resultado)
            if maior < resultado:
                maior = resultado
print(maior)
        