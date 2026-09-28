from random import randint
computador = randint (0,5) # Faz o computador pensar
print('~=~'*30)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('~=~'*30)
jogador = int(input('Em que número pensei?'))
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
              