class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

vitor = Cliente('Vitor', '9999-8888')
print(vitor.nome)