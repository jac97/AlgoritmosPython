#Entrada de dados
valor1, valor2, valor3 = input('Digite três números inteiros diferentes entre si e separados por vírgula seguida de espaço: ').split(', ')
#Conversão de dados
valor1 = int(valor1)
valor2 = int(valor2)
valor3 = int(valor3)

#Processamento de dados
#Menor valor
if valor1 < valor2 and valor1 < valor3:
  menor = valor1
elif valor2 < valor1 and valor2 < valor3:
  menor = valor2
else:
  menor = valor3
#Maior valor
if valor1 > valor2 and valor1 > valor3:
  maior = valor1
elif valor2 > valor1 and valor2 > valor3:
  maior = valor2
else:
  maior = valor3
#Soma dos dois menores
if valor1 > valor2 and valor1 > valor3:
  soma = valor2 + valor3
elif valor2 > valor1 and valor2 > valor3:
  soma = valor1 + valor3
else:
  soma = valor1 + valor2
#Ordem crescente dos valores
if valor1 < valor2 and valor2 < valor3:
  minimo = valor1
  médio = valor2
  máximo = valor3
elif valor2 < valor1 and valor1 < valor3:
  minimo = valor2
  médio = valor1
  máximo = valor3
elif valor3 < valor1 and valor1 < valor2:
  minimo = valor3
  médio = valor1
  máximo = valor2
elif valor2 < valor3 and valor3 < valor1:
  minimo = valor2
  médio = valor3
  máximo = valor1
elif valor3 < valor2 and valor2 < valor1:
  minimo = valor3
  médio = valor2
  máximo = valor1
else:
  minimo = valor1
  médio = valor3
  máximo = valor2

#Saíde de dados
print(f'\nMenor número digitado: {menor}')
print(f'Maior número digitado: {maior}')
print(f'Soma dos dois números menores: {soma}')
print(f'Números digitados, em ordem crescente: {minimo}, {médio}, {máximo}.')