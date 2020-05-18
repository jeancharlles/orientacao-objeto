from modificadores_de_acesso.classe_BaseDeDados import BaseDeDados

if __name__ == '__main__':
    bd = BaseDeDados()
    print(f'-'*60)

    print(bd)
    print(bd.dados)  # Aqui eu consigo acessar por que foi usado @property de forma correta

    bd.inserir_cliente(1, 'joão')
    bd.inserir_cliente(2, 'jonas')

    print(f'-'*60)

    print(bd._dados)  # Aqui eu consigo acessar por que é protegido mas nem tanto, e não é a forma Pythonica

    print(f'-'*60)

    bd.lista_clientes()

    print(f'-'*60)

    bd.apaga_cliente(1)
    bd.lista_clientes()

    # Se esta linha abaixo for ativada, bagunçará a classe pois está protegida mas pode ser alterada
    # bd.__dados = 'Qualquer coisa'
    print(f'-'*60)
    print(bd.dados)  # Aqui eu consigo acessar por que foi usado @property de forma correta

    bd.inserir_cliente(3, 'ana')
    bd.inserir_cliente(4, 'maria')

    print(f'-'*60)
    bd.lista_clientes()
