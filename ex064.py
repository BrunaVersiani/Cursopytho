'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag).'''
print('\033[35m*-' * 30)
valor = cont = soma = 0
valor = int(input('Digite um número ou 999 para parar o programa: '))
while valor != 999:
    cont += 1
    soma += valor
    valor = int(input('Digite um número ou 999 para parar o programa: '))
print('Foram digitados {} números e a soma entre eles e de {}. '.format(cont, soma))
print('*-' * 30)
