import datetime


class Historico:
    def __int__(self, data_abertura, transacoes):
        transacoes = list()
        data_abertura = datetime.datetime.today()
        self.data_abertura = data_abertura
        self.transacoes = transacoes

    def imprime(self):
        print(f'data abertura: {self.data_abertura}', )
        print('transacoes: ')
        for t in self.transacoes:
            print('-', t)


class Conta:

    def __init__(self, numero, cliente, saldo, limite=1000):
        print("inicializando uma conta")
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append()

    def saca(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente')
            return False
        else:
            self.saldo -= valor
            print('Saque realizado com sucesso')
            self.historico.transacoes.append('saque de {}'.format(valor))
            return True

    def transfere(self, destino, valor):
        retirada = self.saca(valor)
        if retirada is False:
            print('Transferência não realizada')
        else:
            destino.saldo += valor
            self.historico.transacoes.append('transferência de {}'.format(valor))
            print('Transferência realizada com sucesso')

    def extrato(self):
        return f'{self.numero} {self.titular.nome} {self.saldo} {self.limite}'

    def pega_saldo(self):
        return self.saldo


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
