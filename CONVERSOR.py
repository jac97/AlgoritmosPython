#Mensagem explicativo de boas vindas!
print('\tOLÁ! SEJA MUITO BEM VINDO/A AO SITE DE CONVERSÃO DE MOEDA.\n')
print('Aqui você consegue fazer a conversão do seu dinheiro em reais para seis (6) diferentes moedas internacionais.')
print('Confira abaixo a tabela de taxa de câmbio atual:\n')
print('\t','+' * 64) #essa linha de código imprime até 64 vezes o caráter "+"
print('\t | 1 real ----------------------------> 0,16 Euro               |')
print('\t | 1 real ----------------------------> 20,67 Iene Japonês      |')
print('\t | 1 real ----------------------------> 1,15 Yuan Chinês        |')
print('\t | 1 real ----------------------------> 0,18 Dolár Americano    |')
print('\t | 1 real ----------------------------> 13,33 Rublo Russo       |')
print('\t | 1 real ----------------------------> 18,05 Peso Argentino    |')
print('\t','+' * 64, '\n') 

#Entrada de dados por parte do usuário
reais_digitado = float(input('Agora que conferiu a tabela, por favor informe o valor (em reais) para a conversão: '))
print('\n') #Essa linha de código serve para dar um Enter entre o valor digitado e o resultado da saída para o usuário

#Processo de conversão do valor digitado para os valores desejados (Processamento de dados)
'''
Para converter o valor digitado (em reais) pelo usuário, basta pegar o valor digitado e multiplicar pela taxa de conversão da moeda desejada.
Ex.: (valor digitado * taxa de câmbio da moeda desejada)
O nome das variáveis nesse processo é formada pelo valor (em reais) digitado seguida pela moeda desejada na conversão, separada por um "_" .
Obs: Essas taxas de câmbio de conversão podem variar de acordo com a atualização mundial, no momento trabalhamos com essas taxas atual.
'''
reais_euro = reais_digitado * 0.16
reais_iene = reais_digitado * 20.67
reais_yuan = reais_digitado * 1.15
reais_dolár = reais_digitado * 0.18
reais_rublo = reais_digitado * 13.33
reais_peso = reais_digitado * 18.05

#Saída de dados para o usuário
'''
Nesse processo de saída de dados para o usuário, vou utilizar o print com vírgula. E para deixar tudo mais atrativo, também vou utilizar
o '\t' para criar uma identação entre o resultado da conversão e as demais mensagens de saída.
O comando '%010.2f'% serve para imprimir o resultado da conversão com 10 caráteres e duas casas decimais, o '010' significa 10 caráteres com
zeros completando os caracteres inexistentes e o '.2f' sigfica que o valor terá duas casas decimais;
O comando '%.2f'% serve para imprimir o valor digitado com duas casas decimais.
O símbolo de 'R$' no código de saída, serve para acompanhar o valor digitado afim de deixar tudo mais organizado e no padrão certo.
'''
print('\tRESULTADO DA CONVERSÃO DO VALOR (EM REAIS) DIGITADO: \n')
print('\t', '%.2f'%reais_digitado,'R$', 'correspode a', '%010.2f'%reais_euro, 'Euro(s)')
print('\t', '%.2f'%reais_digitado,'R$', 'correspode a', '%010.2f'%reais_iene, 'Iene(s) Japonês')
print('\t', '%.2f'%reais_digitado,'R$', 'correspode a', '%010.2f'%reais_yuan, 'Yuan(s) Chinês')
print('\t', '%.2f'%reais_digitado,'R$', 'correspode a', '%010.2f'%reais_dolár, 'Dolár(es) Americano')
print('\t', '%.2f'%reais_digitado,'R$', 'correspode a', '%010.2f'%reais_rublo, 'Rublo(s) Russo')
print('\t', '%.2f'%reais_digitado,'R$', 'correspode a', '%010.2f'%reais_peso, 'Peso(s) Argentino')
print('\nAgradecemos a sua colaboração, volte sempre que precisar!') #Mensagem de agradecimento que será impresso no final de tudo.