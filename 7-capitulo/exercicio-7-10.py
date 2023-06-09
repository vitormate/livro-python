jogo = [['', '', ''],
        ['', '', ''],
        ['', '', '']]

tabuleiro = f'''
 {jogo[0][0]:1} | {jogo[0][1]:1} | {jogo[0][2]:1}
---+---+---
 {jogo[1][0]:1} | {jogo[1][1]:1} | {jogo[1][2]:1} 
---+---+---
 {jogo[2][0]:1} | {jogo[2][1]:1} | {jogo[2][2]:1}
'''

exemplo = '''
Para jogar basta escolher uma das posições abaixo:

 7 | 8 | 9
---+---+---
 4 | 5 | 6 
---+---+---
 1 | 2 | 3
'''

jogador = 0

print('O "x" começa!')
print(exemplo)

while True:
    if jogador % 2 == 0:
        jogada = int(input('Digite aonde você quer jogar o "x": '))
        
        if jogada not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            continue
        else:
            if jogada in [1, 2, 3]:
                if jogada == 1:
                    if jogo[2][0] == '':
                        jogo[2][0] = 'x'
                    else:
                        continue
                if jogada == 2:
                    if jogo[2][1] == '':
                        jogo[2][1] = 'x'
                    else:
                        continue
                if jogada == 3:
                    if jogo[2][2] == '':
                        jogo[2][2] = 'x'
                    else:
                        continue
            
            if jogada in [4, 5, 6]:
                if jogada == 4:
                    if jogo[1][0] == '':
                        jogo[1][0] = 'x'
                    else:
                        continue
                if jogada == 5:
                    if jogo[1][1] == '':
                        jogo[1][1] = 'x'
                    else:
                        continue
                if jogada == 6:
                    if jogo[1][2] == '':
                        jogo[1][2] = 'x'
                    else: continue
            
            if jogada in [7, 8, 9]:
                if jogada == 7:
                    if jogo[0][0] == '':
                        jogo[0][0] = 'x'
                    else:
                        continue
                if jogada == 8:
                    if jogo[0][1] == '':
                        jogo[0][1] = 'x'
                    else:
                        continue
                if jogada == 9:
                    if jogo[0][2] == '':
                        jogo[0][2] = 'x'
                    else:
                        continue

        jogador += 1
    else:
        jogada = int(input('Digite aonde você quer jogar o "0": '))
        if jogada not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            continue
        else:
            if jogada in [1, 2, 3]:
                if jogada == 1:
                    if jogo[2][0] == '':
                        jogo[2][0] = '0'
                    else:
                        continue
                if jogada == 2:
                    if jogo[2][1] == '':
                        jogo[2][1] = '0'
                    else:
                        continue
                if jogada == 3:
                    if jogo[2][2] == '':
                        jogo[2][2] = '0'
                    else:
                        continue
            
            if jogada in [4, 5, 6]:
                if jogada == 4:
                    if jogo[1][0] == '':
                        jogo[1][0] = '0'
                    else:
                        continue
                if jogada == 5:
                    if jogo[1][1] == '':
                        jogo[1][1] = '0'
                    else:
                        continue
                if jogada == 6:
                    if jogo[1][2] == '':
                        jogo[1][2] = '0'
                    else: continue
            
            if jogada in [7, 8, 9]:
                if jogada == 7:
                    if jogo[0][0] == '':
                        jogo[0][0] = '0'
                    else:
                        continue
                if jogada == 8:
                    if jogo[0][1] == '':
                        jogo[0][1] = '0'
                    else:
                        continue
                if jogada == 9:
                    if jogo[0][2] == '':
                        jogo[0][2] = '0'
                    else:
                        continue
        
        jogador += 1
    
    tabuleiro = f'''
     {jogo[0][0]:1} | {jogo[0][1]:1} | {jogo[0][2]:1}
    ---+---+---
     {jogo[1][0]:1} | {jogo[1][1]:1} | {jogo[1][2]:1} 
    ---+---+---
     {jogo[2][0]:1} | {jogo[2][1]:1} | {jogo[2][2]:1}
    '''
    print(tabuleiro)
    
    zero = ['0','0','0']
    xis = ['x', 'x', 'x']
    if zero == jogo[0] or zero == jogo[1] or zero == jogo[2] or zero == [jogo[0][0], jogo[1][1], jogo[2][2]] or zero == [jogo[2][0], jogo[1][1], jogo[0][2]] or zero == [jogo[0][0], jogo[1][0], jogo[2][0]] or zero == [jogo[0][1], jogo[1][1], jogo[2][1]] or zero == [jogo[0][2], jogo[1][2], jogo[2][2]]:
        print('0 venceu!')
        break
    elif xis == jogo[0] or xis == jogo[1] or xis == jogo[2] or xis == [jogo[0][0], jogo[1][1], jogo[2][2]] or xis == [jogo[2][0], jogo[1][1], jogo[0][2]] or xis == [jogo[0][0], jogo[1][0], jogo[2][0]] or xis == [jogo[0][1], jogo[1][1], jogo[2][1]] or xis == [jogo[0][2], jogo[1][2], jogo[2][2]]:
        print('x venceu!')
        break
    elif '' not in jogo[0] and '' not in jogo[1] and '' not in jogo[2]:
        print('Deu velha!')
        break