ESPACO = '  '

class Conta:
    def __init__(self, clientes, número, saldo = 0):
        self.clientes = clientes
        self.número = número
        self.saldo = 0
        self.operacoes = []
        self.deposito(saldo)
    
    def resumo(self):
        print(f"CC Número: {self.número}")
        print(f'Saldo: {self.saldo}')
        print('Proprietários: ')
        for cliente in self.clientes:
            print(f'{ESPACO}Nome: {cliente.nome} | Telefone: {cliente.telefone}')
        print()

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -=valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            print('Saldo insuficiente!')
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f'Extrato CC N° {self.número}')
        for o in self.operacoes:
            print(f'{ESPACO}{o[0]}: {o[1]}')
        print(f'{ESPACO}Saldo: {self.saldo} \n')


class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        super().__init__(clientes, número, saldo)
        self.limite = limite
    
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            return True
        else:
            return False