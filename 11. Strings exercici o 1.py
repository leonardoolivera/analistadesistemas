#escrever uma função que recebe uma lista de strings contendo nomes de pessoas como parametro e devolve o nome mais curto. A função deve ignorar espaços antes e depois do nome e deve apenas devolver o nome capitalizado ---------------------------------------

listaNomes = []
nome = ""

while  nome != "0":
  nome = (str(input("Digite os nomes e ao terminar digite 0.").title().strip()))
  if nome != "0":
    listaNomes.append(nome)
listaNomes.sort(key=len)
print("O menor nome é ",listaNomes[0],"e o maior é ",listaNomes[-1])