#Entrada de dados
operando1 = float(input('Por favor, digite o primeiro operando: '))
operando2 = float(input('Por favor, digite o segundo operando: '))

print('\n******************************')
print('Operações Aritméticas: ')
print(f'\t1) Adição')
print(f'\t2) Subtração')
print(f'\t3) Divisão')
print(f'\t4) Multiplicação')
print(f'\t5) Exponenciação')
print(f'\t6) Resto da divisão')
print(f'\t7) Quociente da divisão')
print('******************************')

operação = int(input('Por favor, digite a operação: '))
print('\n')

#Processamento e Saída de dados
if operação != 1 and operação != 2 and operação != 3 and operação != 4 and operação != 5 and operação != 6 and operação != 7:
  print('Operação Aritmética digitada inválida, por favor tente de novo!')
elif operação == 1:
  resultado = operando1 + operando2
  print(f'Resultado: {operando1:.1f} + {operando2:.1f} = {resultado:.1f}')
elif operação == 2:
  resultado = operando1 - operando2
  print(f'Resultado: {operando1:.1f} - {operando2:.1f} = {resultado:.1f}')
elif operação == 3:
  resultado = operando1 / operando2
  print(f'Resultado: {operando1:.1f} / {operando2:.1f} = {resultado:.1f}')
elif operação == 4:
  resultado = operando1 * operando2
  print(f'Resultado: {operando1:.1f} * {operando2:.1f} = {resultado:.1f}')
elif operação == 5:
  resultado = pow(operando1, operando2)
  print(f'Resultado: {operando1:.1f} ^ {operando2:.1f} = {resultado:.1f}')
elif operação == 6:
  resultado = operando1 % operando2
  print(f'Resultado: {operando1:.1f} % {operando2:.1f} = {resultado:.1f}')
else:
  resultado = operando1 // operando2
  print(f'Resultado: {operando1:.1f} // {operando2:.1f} = {resultado:.1f}')