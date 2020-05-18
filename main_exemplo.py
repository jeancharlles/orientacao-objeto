from classes.classe_exemplo import Pessoa

# Usando método da instância
p0 = Pessoa('Jean', 50)
print(f'Nome: {p0.nome}, Idade: {p0.idade} anos')

# Usando método classmetod
p1 = Pessoa.get_ano_nascimento(1969)
print(p1)

# Usando método staticmethod
p2 = Pessoa.gera_id()
print(p2)
