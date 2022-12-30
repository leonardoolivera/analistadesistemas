
fatores_primos = []
numero_fatorado = 600851475143

i = 2
while numero_fatorado != 1:
  if numero_fatorado % i == 0:
    fatores_primos.append(i)
    numero_fatorado = numero_fatorado / i
  else:
    i += 1
print(fatores_primos)
print("O maior numero primo de 600851475143 é",fatores_primos[-1])