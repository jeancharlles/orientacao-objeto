def teste(arg, *args):
    print('primeiro argumento normal: {}'.format(arg))
    for arg in args:
        print('outro argumento: {}'.format(arg))


def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))


if __name__ == '__main__':

    teste('python', 'é', 'muito', 'legal')

    minha_funcao(chave1=1, chave2=2, chave3='valor3')
