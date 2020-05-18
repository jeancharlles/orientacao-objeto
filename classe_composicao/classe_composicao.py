class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = list()

    def insere_endereco(self, c, e):
        self.enderecos.append(Endereco(c, e))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'Cliente {self.nome} foi apagado')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'Endereco {self.cidade}/{self.estado} foi apagado')


if __name__ == '__main__':

    cliente1 = Cliente('Jean', 50)
    cliente1.insere_endereco('São Paulo', 'SP')
    cliente1.insere_endereco('Rio de Janeiro', 'RJ')
    print(cliente1.nome, cliente1.idade)
    cliente1.lista_enderecos()
    print()
    del cliente1  # Comente esta linha para ver o resultado diferente

    print()

    cliente2 = Cliente('Ana', 46)
    cliente2.insere_endereco('Vitória', 'ES')
    print(cliente2.nome, cliente2.idade)
    cliente2.lista_enderecos()
    print()
    del cliente2  # Comente esta linha para ver o resultado diferente

    print(f'*'*60)
