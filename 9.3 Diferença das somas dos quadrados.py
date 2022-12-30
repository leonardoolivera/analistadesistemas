primeiros_100_quadrado = []
lista_100 = []
contador = 1
quadrado = 1
#define a lista dos quadrados dos primeiros 100 numeros
while  contador <= 100:
    quadrado = contador ** 2
    primeiros_100_quadrado.append(quadrado)
    contador += 1
#   print("Quadrado dos primeiros 100 numeros -",primeiros_100_quadrado)
#somar os quadrados dos primeiros 100 numeros
soma1 = 0
for i in range(len(primeiros_100_quadrado)):
    soma1 = soma1 + primeiros_100_quadrado[i]
print("A soma dos quadrados é :",soma1)

#definir a lista de 100 primeiros numeros
contador = 1
while contador <= 100:
    lista_100.append(contador)
    contador += 1
    
#soma os primeiros 100 numeros
soma = 0
for i in range(len(lista_100)):
    soma = soma + lista_100[i]
print("A soma dos primeiros 100 numeros é ",soma)
soma = soma ** 2
print("O quadrado da soma dos primeiros 100 numeros é ",soma)
#diferença entre a soma dos quadrados dos primeiros cem números naturais e o quadrado da soma
diferença = soma - soma1
print("A diferença entre a soma dos quadrados dos primeiros 100 numeros e o quadrado da soma dos primeiros 100 é ", diferença)
