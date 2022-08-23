'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
#Número primo é um numero que só divisivel por 1 e por ele mesmo.
num = int(input('Digite um número: '))
tot = 0
for p in range(1, num + 1):
    if num % p == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(p), end='')
print('\033[mO número {} foi divisível {} vezes '.format(num, tot), end='')
if tot == 2:
    print('\033[34me por isso ele é PRIMO.')
else:
    print('\033[31me por isso ele não é PRIMO.')
