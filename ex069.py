'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
print('\033[33m§'*30)
print('{:^30}'.format('CADASTRAMENTO'))
print('§' * 30)
cont = maior = menor20 = 0
while True:
    nome = str(input('Digite o nome: ')).upper().strip()
    idade = int(input(f'Quantos anos o {nome} tem? '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Gênero [F/M]: ')).upper().strip()[0]
    if idade > 18:
            maior += 1
    if sexo == 'M':
        cont += 1
    if sexo == 'F':
        if idade < 20:
            menor20 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continiar? [S/N]: ')).upper().strip()
    if continua == 'N':
        break
print(f'A quantidade de pessoas com mais de 18 anos é de {maior}')
print(f'A quantidae de homens cadastrados foi de {cont}')
print(f'A quantidade de mulheres com menos de 20 anos é de {menor20}')
