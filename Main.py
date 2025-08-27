class Main:
    nome = "Ana"
    print(len(nome))

print('Testando o projeto')

from Cliente import Cliente

from Conta import Conta

c1 = Cliente('João', '114444-2222')
conta = Conta(c1., 6565, 0)

print(conta.titular, ' Número: ', conta.numero, 'Seu Saldo: ', conta.saldo)
