'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''\033[36m    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        somar = n1 + n2
        print('\033[33mA soma de {} + {} é {}.'.format(n1, n2, somar))
    elif opção == 2:
        mult = n1 * n2
        print('\033[33mA multiplicação de {} + {} é {}.'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            print('\033[33mO valor {} é maior que {}.'.format(n1, n2))
        else:
            print('\033[33mO valor {} é maior que {}.'.format(n2, n1))
    elif opção == 4:
        n1 = int(input('\033[33m1º valor: '))
        n2 = int(input('\033[33m2º valor: '))
    elif opção == 5:
        opção = 5
    else:
        print('\033[33mOpção inválida! Tente novamente. \033[m')
print('\033[35mFim do programa! ')
