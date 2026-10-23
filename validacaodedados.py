sexo = input('Informe seu sexo [M/F]:').strip().upper()
while sexo not in['M', 'F']:
    sexo = input('Valor inválido! Por favor,digite apenas M ou F: ').strip().upper()

print("Sexo '{sexo}'registrado com sucesso!")