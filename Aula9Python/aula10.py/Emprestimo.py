casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de finaciamento?'))
prestação = casa / (anos * 12)
minímo = salário * 30 / 100
print ('Para pagar uma casa de R$ {:.2f} em {} anos'.format (casa, anos), end='')
print ('A prestação será de R$ {:.2f}'.format(prestação))
if prestação <= minímo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')