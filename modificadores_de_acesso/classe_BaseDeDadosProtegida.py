
class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' in self.__dados:
            self.__dados['clientes'].update({id: nome})
        else:
            self.__dados['clientes'] = {id: nome}

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

    @property
    def dados(self):
        return self.__dados

