#Classe Retangulo: Crie uma classe que modele um retangulo:
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class retangulo():
    def __init__(self,comprimento,largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def mudarValor(self,comprimento,largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def retornarValor(self):
        print("Comprimento ",self.comprimento,"Largura ",self.largura)

    def calculaPerimetro(self):
        x = 2 * (self.comprimento + self.largura)
        return x
        
if __name__ == '__main__':
    retangulo_teste = retangulo(2,19)
    retangulo_teste.calculaPerimetro()
    retangulo_teste.retornarValor()

#na verdade ele ta calculando o perimetro e dividindo por um valor aleatorio
#o correto seria descobrir a area e dividir pelo numero do tamanho do piso

#da pra criar uma classe piso com atributo tamanho, calcular a area do piso e assim dividir a area do retangulo pela area do piso
