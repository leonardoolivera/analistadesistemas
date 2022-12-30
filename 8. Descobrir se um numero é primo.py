#Um número primo é um número natural maior que 1 que não tem mais divisores naturais além dele mesmo e da unidade.
#Não existe formula para descobrir se é um numero primo ou nao, mas podemos usar a divisão para descobrir se ele é divisivel por algum numero alem de 1 e dele mesmo

#para ser considerado primo, o numero precisa ser divisivel por ele mesmo ou por 1.
#ex: o usuario digita 8, entao o algoritmo precisa dividi-lo por 2,3,4,5,6 e 7. Caso alguma dessas divisoes de (%) resto 0 entao o numero não sera considerado primo.


#pede ao usuario que digite um numero

#numeroConferir = int(input("Digite um numero"))

#define um contador

#i = 2

#confere se o numero é positivo e maior que 1

#if numeroConferir <= 1:
#    print("Não é primo")
#else:
#
#recebe o numero e o didide por 2
#
#    while (numeroConferir % i != 0) & (numeroConferir > i):
#        i += 1
#    if numeroConferir % i == 0:
#        print("Não é um numero primo")
#    else: print("É um numero primo")

def is_prime(n):
  if n <= 1:
    return print("Digite um numero maior que 1")
  i = 2
  while i < n:
    if n % i == 0:
      return print("Este numero não é primo")
    i += 1
  return print("Primo rico")

checarNumero = int(input("Digite um numero maior que 2 "))
is_prime(checarNumero)

    
