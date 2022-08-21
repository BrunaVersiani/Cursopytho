'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
 atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano do seu nascimento com os 4 digitos: '))
idade = ano - nasc
if idade <= 9:
    print(' Com {} anos de idade, a sua categoria é \033[45mMIRIM\033[m'.format(idade))

elif idade <= 14 and idade >= 10:
    print(' Com {} anos de idade, a sua categoria é \033[41mINFANTIL\033[m'.format(idade))

elif idade <= 19 and idade >= 11:
    print(' Com {} anos de idade, a sua categoria é \033[42mJÚNIOR\033[m'.format(idade))

elif idade <= 25 and idade >= 20:
    print(' Com {} anos de idade, a sua categoria é \033[43mSÊNIOR\033[m'.format(idade))

elif idade >= 26:
    print(' Com {} anos de idade, a sua categoria é \033[44mMASTER\033[m'.format(idade))
