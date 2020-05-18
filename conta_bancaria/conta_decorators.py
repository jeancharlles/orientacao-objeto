"""
Este código está apresentando falhas
"""


class Conta:
    def __int__(self, saldo=0):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
