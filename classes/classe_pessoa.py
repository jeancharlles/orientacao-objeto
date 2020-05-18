from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.today().year)

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def identificar(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos!')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} não pode comer outro alimento pois ele já está comendo.')
            return

        print(f'{self.nome} está comendo {alimento} ')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não pode parar de comer pois ele não está comendo.')
            return

        print(f'{self.nome} parou de comer agora.')
        self.comendo = False

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} não pode falar de outro assunto pois já está falando.')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar pois está comendo.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        if self.comendo:
            print(f'{self.nome} não está falando, está comendo.')
            return

        if self.falando:
            print(f'{self.nome} parou de falar agora')
            self.falando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


if __name__ == '__main__':
    print(__name__)
