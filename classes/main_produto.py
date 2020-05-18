from classes.classe_produto import Produto

if __name__ == '__main__':

    p1 = Produto('CANETA', 1000)
    print(f'Produto: {p1.nome} - Preço: {p1.preco}')
    p1.desconto(15)
    print(f'Produto: {p1.nome} - Preço: {p1.preco}')

    print()

    p2 = Produto(1, 'R$100')
    print(f'Produto: {p2.nome} - Preço: {p2.preco}')
    p2.desconto(10)
    print(f'Produto: {p2.nome} - Preço: {p2.preco}')
