class Conta:
    def __init__(self, titular, saldo):
        print("inicializando uma conta2")
        self._titular = titular
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        if saldo < 0:
            print('Saldo não pode ser negativo')
        else:
            print('Novo saldo atribuído')
            self._saldo = saldo

    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular

    def pega_saldo(self):
        return self._saldo
