class ser_humano:
    def __init__(self, nome, idade, hooby, profissao):
        self.nome = nome
        self.idade = idade
        self.hobby = hooby
        self.profissao = profissao

    def falar_sobre(self):
        print("Meu nome é ",self.nome,", tenho",self.idade,", gosto de ",self.hobby," e minha profissão é ",self.profissao)

lista = []
while True:
    nome = input("Digite o nome (digite sair para terminar")
    if nome.lower() == "sair":
        break
    idade = input("Digite a idade")
    hooby = input("Digite o hobby")        
    profissao = input("Digite a profissão")
    lista.append(ser_humano(nome, idade, hooby, profissao))
    lista.falar_sobre()
