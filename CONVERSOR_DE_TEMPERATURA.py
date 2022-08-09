#Entrada de dados
temperatura = float(input('Digite a temperatura a ser convertida (em graus): '))

print('\n***********************')
print('Operações de Conversão:')
print(f'\t1: Celsius para Fahrenheit')
print(f'\t2: Celsius para Kelvin')
print(f'\t3: Fahrenheit para Celsius')
print(f'\t4: Fahrenheit para Kelvin')
print(f'\t5: Kelvin para Fahrenheit')
print(f'\t6: Kelvin para Celsius')
print('***********************\n')

operação = int(input('Digite a operação de conversão: '))

#Processamento e Saída de dados
if operação != 1 and operação != 2 and operação != 3 and operação != 4 and operação != 5 and operação != 6:
  print(f'Operação ({operação}) inválida! Por favor, tente novamente.') 
else:
  if (operação == 1):
    convertido = (9 / 5 * temperatura) + 32
    print(f'\nResposta: {temperatura:.2f} graus Celsius equivalem a {convertido:.2f} graus Fahrenheit.')
  elif (operação == 2):
    convertido = temperatura + 273
    print(f'\nResposta: {temperatura:.2f} graus Celsius equivalem a {convertido:.2f} Kelvin.')
  elif (operação == 3):
    convertido = 5 / 9 * (temperatura - 32)
    print(f'\nResposta: {temperatura:.2f} graus Fahrenheit equivalem a {convertido:.2f} graus Celsius.')
  elif (operação == 4):
    convertido = 5 / 9 * (temperatura - 32) + 273
    print(f'\nResposta: {temperatura:.2f} graus Fahrenheit equivalem a {convertido:.2f} Kelvin.')
  elif (operação == 5):
    convertido = (9 / 5 * (temperatura - 273)) + 32
    print(f'\nResposta: {temperatura:.2f} Kelvin equivalem a {convertido:.2f} graus Fahrenheit.')
  else:
    convertido = temperatura - 273
    print(f'\nResposta: {temperatura:.2f} Kelvin equivalem a {convertido:.2f} graus Celsius.')