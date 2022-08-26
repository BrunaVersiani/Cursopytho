'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
print('\033[32m§'*30)
print('{:^30}'.format('JOGO PAR OU IMPAR'))
print('-' * 30)
from random import randint
v = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Escolha PAR ou IMPAR [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador} total = {total}', end='')
    print(' que é PAR.' if total % 2 == 0 else ' que é IMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu! Vamos jogar novamente? ')
            v += 1
        else:
            print(f'Você perdeu! O total de vitorias foi {v}. ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu! Vamos jogar novamente? ')
            v += 1
        else:
            print(f'Você perdeu! O seu total de vitorias foi {v} vez(es)! ')
            break
print('§' * 30)
