#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios
class conta_corrente:
    def __init__(self, numero_conta,nome_correntista,saldo = 0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self,nome):
        self.nome = nome

    def deposito(self,valor):
        self.saldo += valor

    def saque(self,valor):
        if self.saldo <= 0:
            print("Voce n tem saldo seu pobre")
        self.saldo -= valor

    def extrato(self):
        print(self.saldo)

correntista = conta_corrente(2394174,'Leonardo')
correntista.deposito(250)
print(correntista.saldo)
correntista.deposito(500)
print(correntista.saldo)
correntista.saque(600)
print(correntista.saldo)