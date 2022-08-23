'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
 a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomemaisvelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO M/F: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho é {} e tem {} de idade.'.format(nomemaisvelho, maioridadehomen))
print('Ao todo tem {} mulheres tem menos de 20 anos.'.format(totmulher20))


