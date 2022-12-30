import math

n = int(input("Digite o cojunto de elementos n: "))
k = int(input("Digite o cojunto de elementos a serem calculados n: "))

if n < k:
    print("Os numuero de elementos do conjunto não pode ser menor que o do subconjunto")
comb = math.comb(n,k)
print(comb)

