'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
 usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
print('\033[34m§'*30)
print('{:^30}'.format('CADASTRAMENTO'))
print('§' * 30)
total = maismil = maisbarato = 0
while True:
    nome = str(input('Digite o nome do produto: ')).upper().strip()
    preço = float(input('Digite o preço do produto: R$ '))
    total = total + preço
    barato = ' '
    if preço > 1000:
        maismil += 1
    if total == 1 or preço < maisbarato:
        maisbarato = preço
        barato = nome

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break

print('§' * 30)
print(f'O total da compra é R${total:.2f}.')
print(f'O produto mais barato é {barato}.')
print(f'{maismil} itens com preço maior de R$1000,00.')
print('§' * 30)
