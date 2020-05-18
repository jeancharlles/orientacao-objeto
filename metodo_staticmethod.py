class Conta:
    _total_contas = 0

    def __init__(self, saldo=0.0):
        Conta._total_contas += 1
        self._saldo = saldo

    @staticmethod
    def get_total_contas():
        return Conta._total_contas
