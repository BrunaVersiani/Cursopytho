'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
computador = randint(0, 10) #Computador pensa
print('-*-' * 20)
print('Sou seu computador, acabei de pensar em um número entre 0 e 10. Tente adivinhar qual é ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))  # Jogador adivinha o número
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou, com {} tentativas, Parabéns!'.format(palpites))
print('-*-' * 20)

