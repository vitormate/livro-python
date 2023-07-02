from estado import Estado, Cidade

pe = Estado('Pernambuco', 'PE')
ce = Estado('Ceará', 'CE')
pa = Estado('Paraíba', 'PB')

ca = Cidade('Camaragibe', 150)
re = Cidade('Recife', 300)
fo = Cidade('Fortaleza', 300)
ju = Cidade('Juazeiro do Norte', 100)
jp = Cidade('João Pessoa', 300)
pt = Cidade('Patos', 50)


pe.add_cidade(ca)
pe.add_cidade(re)
ce.add_cidade(fo)
ce.add_cidade(ju)
pa.add_cidade(jp)
pa.add_cidade(pt)

pe.populacao_estado()
ce.populacao_estado()
pa.populacao_estado()