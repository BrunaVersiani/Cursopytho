'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
 qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal'''
número = int(input('Digite um numero inteiro: '))
conversão = (int(input('Digite uma opção: 1 para binário, 2 para octal e 3 para hexadecimal. ')))
if conversão == 1:
    print('Você escolheu opção 1 para binário, \033[4;30;42m resultado: {} para {} \033[m'.format(número, bin(número)[2:]))
elif conversão == 2:
    print('Você escolheu opção 2 para octal, \033[4;30;42m resultado: {} para {} \033[m '.format(número, oct(número)[2:]))
elif conversão == 3:
    print('Você escolheu opção 3 para hexadecimal, \033[4;30;42m resultado: {} para {} \033[m '.format(número, hex(número)[2:]))
else:
    print('\033[4;30;41m Opção INVÁLIDA! \033[m ')

