from modificadores_de_acesso.classe_BaseDeDadosProtegida import BaseDeDados

if __name__ == '__main__':
    bd = BaseDeDados()
    print(f'-'*60)

    print(bd)
    print(bd.dados)  # Aqui eu consigo acessar por que foi usado @property de forma correta

    bd.inserir_cliente(1, 'joão')
    bd.inserir_cliente(2, 'jonas')

    print(f'-'*60)

    # print(bd.__dados)  # Aqui eu consigo acessar por que é protegido mas nem tanto, e não é a forma Pythonica

    print(f'-'*60)

    bd.lista_clientes()

    print(f'-'*60)

    bd.apaga_cliente(1)
    bd.lista_clientes()

    # Não é a forma correta, pois o atributo está protegido, e será um nome similar a este na classe protegendo-a
    bd.__dados = 'Qualquer coisa'
    print(bd.__dados) # Não é a forma correta de acessar o atributo protegido dados
    print(bd._BaseDeDados__dados)  # Esta é a forma erra de acessar o atributo protegido dados
    print(f'-'*60)
    print(bd.dados)  # Aqui eu consigo acessar por que foi usado @property de forma correta

    bd.inserir_cliente(3, 'ana')
    bd.inserir_cliente(4, 'maria')

    print(f'-'*60)
    bd.lista_clientes()
