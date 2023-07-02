class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome 
        self.sigla = sigla
        self.cidades = []
    
    def add_cidade(self, cidade):
        self.cidades.append(cidade)
    
    def listar_cidades(self):
        for c in self.cidades:
            print(c.nome)
    
    def populacao_estado(self):
        soma = 0
        for c in self.cidades:
            soma += c.populacao
        print(f'{self.nome}: {soma} habitantes')
        


class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

# Resposta do Site
# class Estado:
#     def __init__(self, nome, sigla):
#         self.nome = nome
#         self.sigla = sigla
#         self.cidades = []

#     def adiciona_cidade(self, cidade):
#         cidade.estado = self
#         self.cidades.append(cidade)

#     def população(self):
#         return sum([c.população for c in self.cidades])


# class Cidade:
#     def __init__(self, nome, população):
#         self.nome = nome
#         self.população = população
#         self.estado = None

#     def __str__(self):
#         return f"Cidade (nome={self.nome}, população={self.população}, estado={self.estado})"