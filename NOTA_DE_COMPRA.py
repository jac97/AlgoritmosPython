#Entrada de dados
nome1, preço1, quantidade1 = input('Digite o nome, preço e quantidade do produto 1, separados por vírgula seguida de espaço: ').split(', ')
nome2, preço2, quantidade2 = input('Digite o nome, preço e quantidade do produto 2, separados por vírgula seguida de espaço: ').split(', ')
nome3, preço3, quantidade3 = input('Digite o nome, preço e quantidade do produto 3, separados por vírgula seguida de espaço: ').split(', ')
nome4, preço4, quantidade4 = input('Digite o nome, preço e quantidade do produto 4, separados por vírgula seguida de espaço: ').split(', ')
nome5, preço5, quantidade5 = input('Digite o nome, preço e quantidade do produto 5, separados por vírgula seguida de espaço: ').split(', ')

#Conversão dos valores em reais e inteiros
preço1 = float(preço1)
quantidade1 = int(quantidade1)
preço2 = float(preço2)
quantidade2 = int(quantidade2)
preço3 = float(preço3)
quantidade3 = int(quantidade3)
preço4 = float(preço4)
quantidade4 = int(quantidade4)
preço5 = float(preço5)
quantidade5 = int(quantidade5)

#Sáida & Processamento
print('\n#########################')
print('Nota de Compras')
print('#########################')

if quantidade1 >= 12:
  valor_1 = quantidade1 * preço1
  desconto = valor_1 * 0.20
  valor1 = valor_1 - desconto
  print(f'\t1) {nome1} (R${preço1:.2f}, {quantidade1} unidade(s)): R${valor_1:.2f} - R${desconto:.2f} (desconto) = R${valor1:.2f}')
else:
  valor1 = quantidade1 * preço1
  print(f'\t1) {nome1} (R${preço1:.2f}, {quantidade1} unidade(s)): R${valor1:.2f}')

if quantidade2 >= 12:
  valor_2 = quantidade2 * preço2
  desconto = valor_2 * 0.20
  valor2 = valor_2 - desconto
  print(f'\t2) {nome2} (R${preço2:.2f}, {quantidade2} unidade(s)): R${valor_2:.2f} - R${desconto:.2f} (desconto) = R${valor2:.2f}')
else:
  valor2 = quantidade2 * preço2
  print(f'\t2) {nome2} (R${preço2:.2f}, {quantidade2} unidade(s)): R${valor2:.2f}')

if quantidade3 >= 12:
  valor_3 = quantidade3 * preço3
  desconto = valor_3 * 0.20
  valor3 = valor_3 - desconto
  print(f'\t3) {nome3} (R${preço3:.2f}, {quantidade3} unidade(s)): R${valor_3:.2f} - R${desconto:.2f} (desconto) = R${valor3:.2f}')
else:
  valor3 = quantidade3 * preço3
  print(f'\t3) {nome3} (R${preço3:.2f}, {quantidade3} unidade(s)): R${valor3:.2f}')

if quantidade4 >= 12:
  valor_4 = quantidade4 * preço4
  desconto = valor_4 * 0.20
  valor4 = valor_4 - desconto
  print(f'\t4) {nome4} (R${preço4:.2f}, {quantidade4} unidade(s)): R${valor_4:.2f} - R${desconto:.2f} (desconto) = R${valor4:.2f}')
else:
  valor4 = quantidade4 * preço4
  print(f'\t4) {nome4} (R${preço4:.2f}, {quantidade4} unidade(s)): R${valor4:.2f}')

if quantidade5 >= 12:
  valor_5 = quantidade5 * preço5
  desconto = valor_5 * 0.20
  valor5 = valor_5 - desconto
  print(f'\t5) {nome5} (R${preço5:.2f}, {quantidade5} unidade(s)): R${valor_5:.2f} - R${desconto:.2f} (desconto) = R${valor5:.2f}')
else:
  valor5 = quantidade5 * preço5
  print(f'\t5) {nome5} (R${preço5:.2f}, {quantidade5} unidade(s)): R${valor5:.2f}')

total = valor1 + valor2 + valor3 + valor4 + valor5
print(f'Total de compra: R${total:.2f}')
print('#########################')