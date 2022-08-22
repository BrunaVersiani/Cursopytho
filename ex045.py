#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint
print('\033[36m{:=^30}'.format(' JOKENPÔ '))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''SUAS OPÇÕES:
 PEDRA  => 0
 PAPEL  => 1
TESOURA => 2
NÃO VALE LAGARTO SPOK. RSRSRS''')
jogador = int(input('Qual a sua jogada? '))
print(' JO')
sleep(1)
print(' KEN')
sleep(1)
print(' PÔ...')
sleep(1)
print('{:=^30}'.format(''))
print('O COMPUTADOR ESCOLHEU {}.'.format(itens[computador]))
print('VOCÊ ESCOLHEU {}. '.format(itens[jogador]))
if computador == 0: #pedra
    if jogador == 0:
        print('JOGADA EMPATADA.')
    elif jogador == 1:
        print('O VENCEDOR DA JOGADA É JOGADOR! ')
    elif jogador == 2:
        print('O VENCEDOR DA JOGADA É COMPUTADOR! ')
    else:
        print('JOGAFA INVÁLIDA')

elif computador == 1: #papel
    if jogador == 0:
        print('O VENCEDOR DA JOGADA É COMPUTADOR! ')
    elif jogador == 1:
        print('JOGADA EMPATADA.')
    elif jogador == 2:
        print('O VENCEDOR DA JOGADA É JOGADOR! ')
    else:
        print('JOGAFA INVÁLIDA')
elif computador == 2:#tesoura
    if jogador == 0:
        print('O VENCEDOR DA JOGADA É JOGADOR! ')
    elif jogador == 1:
        print('O VENCEDOR DA JOGADA É COMPUTADOR! ')
    elif jogador == 2:
        print('JOGADA EMPATADA.')
    else:
        print('JOGAFA INVÁLIDA')
print('{:=^30}'.format(''))
