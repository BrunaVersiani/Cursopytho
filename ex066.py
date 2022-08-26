'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
soma entre elas (desconsiderando o flag).'''
print('\33[36m/' * 50)
quant = soma = 0
while True:
    num = int(input('Digite um valor ou digite 999 para parar: '))
    if num == 999:
        break
    quant += 1
    soma += num
print(f'A soma dos valores são {soma} e a quantidade de numeros digitados foi {quant}')
print('\33[36m/' * 50)
