dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

min_para_seg = minutos * 60
horas_para_seg = horas * 3600
dias_para_seg = dias * 86400

total_segundos = dias_para_seg + horas_para_seg + min_para_seg + segundos

print(f'Total em segundos {total_segundos}')