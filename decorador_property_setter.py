class Conta:
    def __init__(self, saldo=0.0):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if self._saldo < 0:
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo
