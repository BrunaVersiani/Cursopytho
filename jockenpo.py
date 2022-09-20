print('''SUAS OPÇÕES:
 PEDRA  => 0
 PAPEL  => 1
TESOURA => 2''')


def jogada(jogador1, jogador2):
    if jogador1 == 0:  # pedra
        if jogador2 == 0:
            print('JOGADA EMPATADA.')
        elif jogador2 == 1:
            print('O VENCEDOR DA JOGADA É JOGADOR2! ')
        elif jogador2 == 2:
            print('O VENCEDOR DA JOGADA É JOGADOR1! ')
        else:
            print('JOGADA INVÁLIDA')

    elif jogador1 == 1:  # papel
        if jogador2 == 0:
            print('O VENCEDOR DA JOGADA É JOORGAD1! ')
        elif jogador2 == 1:
            print('JOGADA EMPATADA.')
        elif jogador2 == 2:
            print('O VENCEDOR DA JOGADA É JOGADOR2! ')
        else:
            print('JOGADA INVÁLIDA')

    elif jogador1 == 2:  # tesoura
        if jogador2 == 0:
            print('O VENCEDOR DA JOGADA É JOGADOR2! ')
        elif jogador2 == 1:
            print('O VENCEDOR DA JOGADA É JOGADOR1! ')
        elif jogador2 == 2:
            print('JOGADA EMPATADA.')
        else:
            print('JOGADA INVÁLIDA')

print('{:=^30}'.format(''))
print(jogada(0, 0))
