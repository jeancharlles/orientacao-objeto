class Conta:

    _total_contas = 0

    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    def __int__(self, saldo=0):
        self._saldo = saldo
        Conta._total_contas += 1

