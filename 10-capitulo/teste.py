from clientes import Cliente
from contas import Conta, ContaEspecial
from bancos import Banco

joao = Cliente('João da Silva', '777-1234')
maria = Cliente('Maria da Silva', '555-4321')
jose = Cliente('José da Silva', '333-7654')


contaJM=Conta([maria, joao], 100)
contaJ=Conta([jose], 10)
contaJJ = Conta([joao, jose], 1, 500)
conta1 = ContaEspecial([maria, joao], 2, 500, 1000)

tatu = Banco('Tatu')
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()

conta1.deposito(300)
conta1.deposito(95.15)
print(conta1.saque(500))
conta1.extrato()
contaJ.saque(500)