class Funcionario:
    __slots__ = ['_nome', '_cpf', '_salario']

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10


class Gerente(Funcionario):
    __slots__ = ['_senha', '_qtd_gerenciados']

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False

    def get_bonificacao(self):
        return super(Gerente, self).get_bonificacao() + 500
        # return self._salario * 0.15
