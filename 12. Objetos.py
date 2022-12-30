class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("Olá, meu nome é", self.nome, "e tenho", self.idade, "anos.")

pessoas = []

while True:
    nome = input("Digite o nome da pessoa (digite 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    idade = int(input("Digite a idade da pessoa: "))
    pessoas.append(Pessoa(nome, idade))
    
for pessoa in pessoas:
    pessoa.falar()

#exerciicios para treinar classes