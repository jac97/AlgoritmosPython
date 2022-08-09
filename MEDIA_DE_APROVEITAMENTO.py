#Entrada de dados
nota1, nota2, nota3, média_exercício = input('Digite na sequência as três notas e a média dos exercícios, separados por espaço: ').split()

#Processo de conversão de dados
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
média_exercício = float(média_exercício)

média_aproveitamento = (nota1 + (nota2 * 2) + (nota3 * 3) + média_exercício) / 7

#Saída de dados
print('\n')
print(f'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(f'+ CONCEITO    |              MÉDIA DE APROVEITAMENTO     +')
print(f'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(f'+     A       |               maior ou igual a 9,0       +')
print(f'+     B       |     maior ou igual a 7,5 e menor que 9,0 +')
print(f'+     C       |     maior ou igual a 6,0 e menor que 7,5 +')
print(f'+     D       |                 menor que 6,0            +')
print(f'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('\n')

if média_aproveitamento >= 9:
  print(f'Conceito final na disciplina: A.')
elif média_aproveitamento >= 7.5 and média_aproveitamento < 9:
  print(f'Conceito final na disciplina: B.')
elif média_aproveitamento >= 6.0 and média_aproveitamento < 7.5:
  print(f'Conceito final na disciplina: C.')
else:
  print(f'Conceito final na disciplina: D.')