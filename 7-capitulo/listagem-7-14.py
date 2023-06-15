s = 'tigre'
print('X'+ s.center(10)+'X')
print('X'+ s.center(10, '.')+'X')

print(s.ljust(20))
print(s.rjust(20))

print(s.ljust(20,'-'))
print(s.rjust(20,'-'))

x = '''asdasd
qweqwe
zxczxczx'''.splitlines()

print(x)

z = 'um gato, dois gatos, três tigres'

print(z.replace(' ', ''))

y = '123'

print(f'{y:=^20}')