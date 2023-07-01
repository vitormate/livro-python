class Televisao:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max

    def mudar_canal_para_cima(self):
        if self.canal < self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin
    
    def mudar_canal_para_baixo(self):
        if self.canal > self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

tv = Televisao(1, 99)
for x in range(0, 100):
    tv.mudar_canal_para_cima()
print(tv.canal)

for x in range(0, 100):
    tv.mudar_canal_para_baixo()
print(tv.canal)