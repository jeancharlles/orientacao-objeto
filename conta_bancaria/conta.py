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
    def __init__(self, numero, cliente_novo, saldo, limite=1000):
        print("Inicializando uma conta")
        self._numero = numero
        self._titular = cliente_novo
        self._saldo = saldo
        self._limite = limite
        # self.historico = Historico()

    def deposita(self, valor):
        print(f'Deposito: R${valor}')
        self._saldo += valor
        # self.historico.transacoes.append(valor)

    def saca(self, valor):
        if self._saldo < valor:
            print(f'Saldo Insuficiente para sacar {valor}')
            return False
        else:
            self._saldo -= valor
            print(f'Saque de {valor} reais realizado com sucesso')
            # self.historico.transacoes.append('saque de {}'.format(valor))
            return True

    def transfere(self, destino, valor):
        retirada = self.saca(valor)
        if retirada is False:
            print('Transferência não realizada')
        else:
            destino._saldo += valor
            # self.historico.transacoes.append('transferência de {}'.format(valor))
            print(f'Transferência de {valor} reais realizada com sucesso')

    def extrato(self):
        return f'{self._numero} {self._titular.nome} {self._saldo} {self._limite}'

    def pega_saldo(self):
        return self._saldo


if __name__ == '__main__':

    cliente = Cliente('João', 'Silva', '123')
    conta1 = Conta(1, cliente, 100)
    print(
        f'Cliente: {cliente.nome} {cliente.sobrenome} \n'
        f'CPF: {cliente.cpf} \n'
        f'Nº Conta: {conta1._numero} \n'
        f'Saldo Inicial: R${conta1._saldo} \n'
        f'Limite: R${conta1._limite} \n'
    )
    conta1.deposita(100)
    print(
        f'Saldo: R${conta1._saldo} \n'
    )
    conta1.saca(50)
    print(
        f'Saldo: R${conta1._saldo} \n'
    )

    cliente = Cliente('Ana', 'Maria', '456')
    conta2 = Conta(2, cliente, 50)
    print(
        f'Cliente: {cliente.nome} {cliente.sobrenome} \n'
        f'CPF: {cliente.cpf} \n'
        f'Nº Conta: {conta2._numero} \n'
        f'Saldo Inicial: R${conta2._saldo} \n'
        f'Limite: R${conta2._limite} \n'
    )
    conta2.transfere(conta1, 10)

    print('\n', '-'*10, 'Histórico', '-'*10)
    print(conta1.extrato())
    print(conta2.extrato())
