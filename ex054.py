'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
ano = date.today().year
cont = 0
totmenor = 0
for n in range(1, 8):
    nasc = int(input('Em qual ano a {}ª pessoa nasceu : '.format(n)))
    idade = ano - nasc
    if idade >= 18:
        cont += 1
    else:
        totmenor += 1
print('Ao total temos {} pessoas maoires de idade '.format(cont), end='')
print('e {} menores de idade. '.format(totmenor))
