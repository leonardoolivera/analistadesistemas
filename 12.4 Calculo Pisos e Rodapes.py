#Crie um programa que utilize a classe retangulo criada anteriormente. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
import Classe_retangulo as classe

x = int(input("Digite a largura "))
y = int(input("Digite o comprimento "))
retangulo1 = classe.retangulo(x,y)
retangulo1.retornarValor()

def quantidade_pisos(x):
    quantidade = x / 10
    print("Serao necessarios ",quantidade,"de pisos")

quantidade_pisos(retangulo1.calculaPerimetro())
print(retangulo1.calculaPerimetro())


