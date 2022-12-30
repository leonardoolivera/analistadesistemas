def busca(sequencia, item_procurado):
    for i in range(len(sequencia)):
        if sequencia[i] == item_procurado:
            return True

sequencia = ['leo','joao','geracy']
if busca(sequencia,'leo') == True:
    print("Encontrado")