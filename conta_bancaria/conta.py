import datetime


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Historico:
    def __int__(self, data_abertura, transacoes):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print('data abertura: {}'.format(self.data_abertura))
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
        # self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        # self.historico.transacoes.append(valor)

    def saca(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente')
            return False
        else:
            self.saldo -= valor
            print('Saque realizado com sucesso')
            # self.historico.transacoes.append('saque de {}'.format(valor))
            return True

    def transfere(self, destino, valor):
        retirada = self.saca(valor)
        if retirada is False:
            print('Transferência não realizada')
        else:
            destino.saldo += valor
            # self.historico.transacoes.append('transferência de {}'.format(valor))
            print('Transferência realizada com sucesso')

    def extrato(self):
        return f'{self.numero} {self.titular.nome} {self.saldo} {self.limite}'

    def pega_saldo(self):
        return self.saldo


if __name__ == '__main__':
    cliente = Cliente('João', 'Silva', '123')
    conta = Conta(1, cliente, 100)
    print(f'Cliente: {cliente.nome} {cliente.sobrenome}')
    print(f'CPF: {cliente.cpf}')
    print(f'Limite: {conta.limite}')
    print(f'Nº Conta: {conta.numero}')
    print(f'Saldo: {conta.saldo}')
    print(f'Limite: {conta.limite}')
