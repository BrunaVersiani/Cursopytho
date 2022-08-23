'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Esta frase é um palíndromo')
else:
    print('Não é uma frase palíndromo')

