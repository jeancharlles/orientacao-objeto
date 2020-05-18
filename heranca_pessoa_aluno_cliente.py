class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'Pessoa {self.nome} está falando.')
        print(f'Classe: {self.nomeclasse}')


class Aluno(Pessoa):
    def estudar(self):
        print(f'Aluno {self.nome} está falando.')


class Cliente(Pessoa):
    def comprar(self):
        print(f'Cliente {self.nome} está falando.')


if __name__ == '__main__':
    p = Pessoa('João', 25)
    print(p.nome, p.idade)
    p.falar()
    print()

    a = Aluno('Joãozinho', 12)
    print(a.nome, a.idade)
    a.estudar()
    print()

    c = Cliente('Maria', 31)
    print(c.nome, c.idade)
    c.comprar()
    print()

    p.falar()
    print()
    a.falar()
    print()
    c.falar()
    print(f'*'*60)

    # Erros uma classe filha não pode usar o método de outra classe somente a própria ou da pai
    # p.estudar()
    # a.comprar()
    # c.estudar()
