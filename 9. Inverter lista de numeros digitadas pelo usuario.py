lista = []

entrada = ()
while entrada != 0:
        #pede para o usuario digitar uma lista de numeros
        entrada = int(input("Digite uma lista de numero terminadas em 0, quando terminar digite 0 para sair"))
        if entrada == 5:
            print("Por favor, digite um numero que termina em 0, não digite o numero 5")
        if (entrada % 5) == 0 or (entrada % 10) == 0:  
            #verifica se o comando parar (0) foi feito
            if entrada != 0:
                #adiciona o numero digitado a lista
                lista.append(entrada)
        else: print("Digite um numero terminado em 0")
#inverte a ordem da lista e imprime na tela (nesse caso usamos o operador slicing ':')        
print(lista) 
for i in lista:
    print(i)








#lista = [1, 2, 3, 4, 5]

#lista[::-1]
#[5, 4, 3, 2, 1]
#No exemplo acima, o slicing é feito da seguinte maneira:

#O primeiro índice (antes do primeiro dois pontos) é o índice inicial da seleção. Como não foi especificado, o índice inicial é o primeiro elemento da lista (índice 0).
#O segundo índice (depois do primeiro dois pontos e antes do segundo) é o índice final da seleção. Como não foi especificado, o índice final é o último elemento da lista (índice -1).
#O terceiro índice (depois do segundo dois pontos) é o passo. Como o passo foi especificado como -1, o slicing é feito da direita para a esquerda.



