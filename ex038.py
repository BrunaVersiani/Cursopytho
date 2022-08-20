'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 > valor2:
    print('O primeiro valor é maior: {} '.format(valor1))
    print('O segundo valor é maior: {} '.format(valor2))

elif valor2 > valor1:
    print('O primeiro valor é maior: {} '.format(valor2))
    print('O segundo valor é maior: {} '.format(valor1))

else:
    print('Não existe valor maior, os dois são iguais. ')
