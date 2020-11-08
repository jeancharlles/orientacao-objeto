class CarrinhoDeCompra:
    def __init__(self):
        self.produtos = list()

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(f'Produto: {produto.nome} - Valor: {produto.valor}')
        print()

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
            print(f'A soma total foi de {total}')
        print()


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


if __name__ == '__main__':

    p1 = Produto('tomate', 5)
    p2 = Produto('mamão', 4)
    p3 = Produto('cacau', 6)
    compra = CarrinhoDeCompra()
    compra.inserir_produto(p1)
    compra.inserir_produto(p2)
    compra.inserir_produto(p3)

    p4 = Produto('café', 3)
    compra.inserir_produto(p4)
    compra.lista_produtos()
    compra.soma_total()
