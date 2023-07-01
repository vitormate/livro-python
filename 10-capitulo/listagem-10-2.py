class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def mudar_canal_para_cima(self):
        self.canal += 1
    
    def mudar_canal_para_baixo(self):
        self.canal -= 1

tv = Televisao()
print(tv.canal)

tv.mudar_canal_para_cima()
tv.mudar_canal_para_cima()
print(tv.canal)

tv.mudar_canal_para_baixo()
print(tv.canal)
