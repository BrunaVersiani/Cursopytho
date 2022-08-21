'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''
peso = float(input('Digite quantos kg você tem: '))
alt = float(input('Didite a sua altura (m): '))
imc = peso / (alt ** 2)
print('\033[mO se IMC é de {:.1f}.\033[m'.format(imc))
if imc < 18.5:
    print('\033[1;43mVocê esta Abaixo do Peso Ideal!\033[m')

elif 18.5 <= imc < 25:
    print('\033[1;42mParabens! Você esta na faixa de peso Ideal!\033[m')

elif 25 <= imc < 30:
    print('\033[1;45mVoce esta em Sobrepeso!\033[m')

elif 30 <= imc < 40:
    print('\033[1;44mVocê está em Obesidade!\033[m')

elif imc >= 40:
    print('\033[1;41mVocê esta em Obesidade Mórbida!\033[m')
