class Conta:
    _total_contas = 0

    def __init__(self, *args):
        type(self)._total_contas += 1

    @classmethod
    def get_total_contas(cls):
        return cls._total_contas
