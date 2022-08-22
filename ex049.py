'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for.'''
num = int(input('Digite um número para ver a sua tabuada: '))
for tab in range(0, 11):
    print('{} x {:2} = {:2}'.format(num, tab, num*tab))
