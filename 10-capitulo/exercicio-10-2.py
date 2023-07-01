class Televisao:
    def __init__(self, canal):
        self.ligada = False
        self.canal = canal
        self.tamanho = '32°'
        self.marca = 'Sansung'

tv = Televisao(4)
print(tv.canal)