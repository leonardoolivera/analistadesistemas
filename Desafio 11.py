import math

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for div in range(3, math.ceil(math.sqrt(x)+ 1), 2):
        if x % div == 0:
            return False
    return True
 
sum = 2
primos_lista = [2]
for i in range(3,2000000,2):
  if i % 2 == 0:
    continue
  if is_prime(i) == True:
    primos_lista.append(i)
    sum = sum + i
print(sum)
