'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano em que você nasceu com quatros digitos: '))
genero = str(input('Qual é o seu Gênero? F ou M ')).upper().strip()
idade = ano - nasc
print('\033[1;36mO ano atual é: {} é você tem {} anos de idade.\033[m'.format(ano, (ano - nasc)))
if genero == 'F':
    print('\033[1;35mO seu sexo é feminino e você não tem obrigação de se alistar!\033[m ')
elif idade < 18:
    falta = 18 - idade
    print('Ainda falta \033[0;33m {} anos \033[m para o alistamento!'.format(falta))
    anoalis = ano + falta
    print('O ano do seu alistamento será em {}.'.format(anoalis))
elif idade == 18:
    print('\033[1;32m Você deve se alistar, neste ANO!\033[m ')
elif idade > 18:
    passou = idade - 18
    print('Você já deveria ter se alistado \033[0;31m há {} anos,\033[m!'.format(passou))
    anoalis = ano - passou
    print('O ano do seu alistamento foi em {}. '.format(anoalis))
else:
    print('Opção INVÁLIDA')
