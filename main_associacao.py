from classe_associacao.classe_associacao import MaquinaDeEscrever, Escritor, Caneta

escritor = Escritor('Jean')
print(f'\nO nome do escritor é {escritor.nome}')

caneta = Caneta('Bic')
print(f'A marca da caneta é {caneta.marca}\n')

maquina = MaquinaDeEscrever()
maquina.escrever()

print()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
print(escritor.ferramenta.marca)

del escritor

print()
print(f'A marca da caneta é {caneta.marca}')
print(caneta.escrever())
maquina.escrever()
