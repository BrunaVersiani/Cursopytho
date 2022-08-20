'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado.'''
casa = float(input('Qual o valor da casa? '))
salário = float(input('Qual valor do salário do comprador? '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação >= (salário * 30 / 100):
    print('Lamento você não conseguiu o emprestimo.')
else:
    print('Parabens! Você foi aprovado na analise para o emprestimo. ')
