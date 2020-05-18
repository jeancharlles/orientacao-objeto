def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero,
             'titular': titular,
             'saldo': saldo,
             'limite': limite}
    return conta


def saca(conta, valor):
    conta['saldo'] -= valor


def deposita(conta, valor):
    conta['saldo'] += valor


def extrato1(conta):
    print(f'Conta: {0} \n Titular: {1} \n Saldo: {2} \n', conta['numero'], conta['titular'], conta['saldo'])


def extrato(conta):
    print(f'Conta: {0} \n'
          f' Titular: {1} \n'
          f' Saldo: {2} \n',
          f'Limite: {3}',
          conta['numero'],
          conta['titular'],
          conta['saldo'],
          conta['limite'])

