#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor
class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor        
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self,cor):
        self.cor = cor
    
    def mostraCor(self):
        print(self.cor)

bola1 = Bola('vermelho',10,'plastico')
bola1.mostraCor()
bola1.trocaCor('azul')
bola1.mostraCor()
