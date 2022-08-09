print('\tTIPOS DE INSTALAÇÕES:')
print('R --------------------------> Residêncial')
print('C --------------------------> Comercial')
print('I --------------------------> Industrial\n')

energia = float(input('Digite a quantidade de energia elétrica consumida (em kW/h): '))
print('\nAtenção: UTILIZE UMA LETRA MAÍUSCULA PARA INFORMAR O TIPO DE INSTALAÇÃO!\n')
instalação = input('Informe o seu tipo de instalação: ')
if instalação != 'R' and instalação != 'C' and instalação != 'I':
  print(f'Tipo de instalação ({instalação}) inválida. Por favor, leia as instruções acima e tente novamente!')
else:
  if (instalação == 'R'):
    if (energia <= 500):
      preço_por_hora = 0.40
    else:
        preço_por_hora = 0.65
  elif (instalação == 'C'):
    if (energia <= 1000):
      preço_por_hora = 0.55
    else:
        preço_por_hora = 0.70
  else:
    if (energia <= 5000):
      preço_por_hora = 0.75
    else:
        preço_por_hora = 0.80

  preço_total = energia * preço_por_hora
  print(f'\nO preço total a pagar pela energia consumida é de: {preço_total:.2f}R$')