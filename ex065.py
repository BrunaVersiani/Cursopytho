'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
 média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
 quer ou não continuar a digitar valores.'''
print('\33[36m~' * 30)
continua = 'S'
num = soma = quant = maior = menor = 0
while continua in 'Ss':
    num = int(input('Digite um número: '))
    continua = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print(f'A quantidade de valores é {quant}.')
print(f'A média de valores é {media}.')
print(f'O Maior valor é {maior} e o Menor {menor}.')
print('~' * 30)
