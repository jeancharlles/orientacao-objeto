"""
Variável de Classe, é interessante alterar a variável de classe e não na instância
"""


if __name__ == '__main__':
    class A:
        vc = 123

    a1 = A()
    a2 = A()
    print(a1.vc)
    print(a2.vc)
    print()

    A.vc = 321
    print(A.vc)
    print(a1.vc)
    print(a2.vc)

