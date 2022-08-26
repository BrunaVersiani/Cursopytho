'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''
print('\33[36m~' * 30)
while True:
    valor = int(input('Digite um valor para ver a sua Tabuada, ou um número negativo para encerrar: '))
    if valor < 0:
        break
    for c in range(1, 11):
        print(f'{valor} x {c} = {valor * c}')
print('Fim!')
print('\33[36m~' * 30)
