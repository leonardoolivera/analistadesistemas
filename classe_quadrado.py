#Classe Quadrado: Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
class Quadrado:
    def __init__(self,tamanho_do_lado,cor):
        self.tamanho_do_lado = tamanho_do_lado
        self.cor = cor

    def mudarValor(self,novoValor):
        self.tamanho_do_lado = novoValor
    
    def retornarValor(self):
        print(self.tamanho_do_lado,self.cor)

    def calcularArea(self):
        print(self.tamanho_do_lado * 2)

quadrado_teste = Quadrado(10,'vermelho')
quadrado_teste.calcularArea()
quadrado_teste.mudarValor(2)
quadrado_teste.calcularArea()
quadrado_teste.retornarValor()
