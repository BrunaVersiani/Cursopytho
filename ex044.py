'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format('LOJAS MAIS'))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: preço formal
[ 4 ] Em 3x ou mais no cartão: 20% de juros ''')
opção = int(input('Escolha uma forma de pagamento? '))
if opção == 1:
    desconto = preço - (preço * 10 / 100)
    print('Você recebeu 10% de desconto, no valor da compra de R${:.2f} você pagará R${:.2f}. '.format(preço, desconto))
elif opção == 2:
    desconto = preço - (preço * 5 /100)
    print('Você recebeu 5% de desconto, no valor da compra de R${:.2f} você pagará R${:.2f}. '.format(preço, desconto))
elif opção == 3:
    print('Você pagará R${:.2f}, sem juros. '.format(preço))
elif opção == 4:
    juros = preço + (preço * 20 / 100)
    print('Você pagará R${:.2f} ao todo, pois tem 20% de juros. '.format(juros))
