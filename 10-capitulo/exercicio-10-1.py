class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = '32°'
        self.marca = 'Sansung'

tv = Televisao()
print(tv.ligada, 
      tv.canal, 
      tv.tamanho, 
      tv.marca)

tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 13
tv_sala.tamanho = '48°'
tv_sala.marca = 'LG'
print(tv_sala.ligada, 
      tv_sala.canal, 
      tv_sala.tamanho, 
      tv_sala.marca)