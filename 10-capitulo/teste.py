from clientes import Cliente
from contas import Conta
from bancos import Banco

joao = Cliente('João da Silva', '777-1234')
maria = Cliente('Maria da Silva', '555-4321')
jose = Cliente('José da Silva', '333-7654')


contaJM=Conta([maria, joao], 100)
contaJ=Conta([jose], 10)

tatu = Banco('Tatu')
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()
