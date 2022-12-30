limite = 4000000
fibonacci = []
termo1 = 0
termo2 = 1
novoTermo = termo1 + termo2
soma = 0
#só vamos adicionar numeros a lista enquanto ele for menor que o limite, por isso o uso do while
while novoTermo <= limite:
    fibonacci.append(novoTermo)
    novoTermo = termo1 + termo2
    termo1 = termo2
    termo2 = novoTermo

#separa os numeros pares da lista e soma
for number in fibonacci:
    if number % 2 == 0:
        soma = soma + number       
#imprimir soma dos numeros pares
print("A soma dos numeros pares de fibonacci até 4 milhões é",soma)
for i in range(len(fibonacci)):
    fibonacci[i] = fibonacci[i]*2
print(fibonacci)
