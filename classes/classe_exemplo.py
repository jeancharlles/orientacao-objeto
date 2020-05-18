from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = int(datetime.today().year)

    # Usando método da instância
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Usando método classmetod
    @classmethod
    def get_ano_nascimento(cls, ano_nascimento):
        return cls.ano_atual - ano_nascimento

    # Usando método staticmethod
    @staticmethod
    def gera_id():
        return randint(0, 10)
