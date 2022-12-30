#Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. A soma desses múltiplos é 23.

#Encontre a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.


listaMultiplos = []
fim = 999
multiplo3 = 3
multiplo5 = 5

#adiciona todos os multiplos de 3 ate 1000 em uma lista  
while fim > 0:
    if (fim % multiplo3 == 0) or (fim % multiplo5 == 0):
        listaMultiplos.append(fim)
        fim = fim - 1
    else: fim = fim - 1
#adiciona todos os multiplos de 5 ate 1000 em uma lista
print(sum(listaMultiplos))

