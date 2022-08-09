#Abaixo está uma string que contém o menu que será apresentado usuário, ele só vai deixar de aparecer se o usuário escolher sair do programa;
menu = ''' \tMenu de Opções:
1 =======================================> Entrar com os dados do horário!
2 =======================================> Sair do programa!
\nEscolha a operação que deseja realizar: '''

while True: #inicio do loop
  opção_de_entrada = input(menu) #imprime o string "menu" logo no início do loop;

  if opção_de_entrada == '1': #Condição para receber os dados do horário
    print('\n')
    #Entrada de dados por parte do usuário
    hora_digitada = int(input('Por gentileza, informe a hora: '))
    minuto_digitado = int(input('Agora, informe o minuto: '))
    print('\n')

#verificar se o formato da hora digitada é válido;
    if hora_digitada >= 0 and hora_digitada <= 23 and minuto_digitado >= 0 and minuto_digitado <= 59:

#verificar se a hora digitada tem menos de dois digitos para poder completar com zero a esquerda;
      if hora_digitada >= 0 and hora_digitada < 10:
        hora_corrigida = str(hora_digitada).zfill(2) #adicionar zero a esquerda da hora, caso tenha apenas um digito;
      else:
        hora_digitada = hora_digitada #caso a hora tiver dois digitos, manter o valor digitado;

#verificar se o minuto digitado tem menos de dois digitos para poder completar com zero a esquerda;
      if minuto_digitado >= 0 and minuto_digitado < 10:
        minuto_corrigido = str(minuto_digitado).zfill(2) #adicionar zero a esquerda da hora, caso tenha apenas um digito;
      else:
        minuto_digitado = minuto_digitado #caso a hora tiver dois digitos, manter o valor digitado;

      #conversão de horas digitadas acima ou igual a 10 para o formato de 12 horas;
      #a variavél hora_convertida recebe a hora correspondente ao formato de 12 horas,
      #quando ela for digitada e estiver entre 10 e 23 horas do formato 24 horas;
      if hora_digitada == 10:
        hora_convertida = '10'
      elif hora_digitada == 11:
        hora_convertida = '11'
      elif hora_digitada == 12:
        hora_convertida = '12'
      elif hora_digitada == 13:
        hora_convertida = '01'
      elif hora_digitada == 14:
        hora_convertida = '02'
      elif hora_digitada == 15:
        hora_convertida = '03'
      elif hora_digitada == 16:
        hora_convertida = '04'
      elif hora_digitada == 17:
        hora_convertida = '05'
      elif hora_digitada == 18:
        hora_convertida = '06'
      elif hora_digitada == 19:
        hora_convertida = '07'
      elif hora_digitada == 20:
        hora_convertida = '08'
      elif hora_digitada == 21:
        hora_convertida = '09'
      elif hora_digitada == 22:
        hora_convertida = '10'
      elif hora_digitada == 23:
        hora_convertida = '11'

#Comando de saída
  #saída do formato 24 horas;
      print(f'CONFIRA O RESULTADO DO HORÁRIO DIGITADO NO FORMATO DE 12 HORAS E TAMBÉM DE 24 HORAS:\n')
      if hora_digitada < 10 and minuto_digitado >= 10:
        print(f'Formato 24 horas => São: {hora_corrigida}h{minuto_digitado}')
      elif hora_digitada < 10 and minuto_digitado < 10:
        print(f'Formato 24 horas => São: {hora_corrigida}h{minuto_corrigido}')
      elif hora_digitada > 10 and minuto_digitado < 10:
        print(f'Formato 24 horas => São: {hora_digitada}h{minuto_corrigido}')
      else:
        print(f'Formato 24 horas => São: {hora_digitada}h{minuto_digitado}')
            
      print('\n')

  #saída do formato 12 horas;
      if hora_digitada >= 0 and hora_digitada < 10:
        if minuto_digitado >= 10:
          print(f'Formato 12 horas => São: {hora_corrigida}:{minuto_digitado} a.m.')
        else:
          print(f'Formato 12 horas => São: {hora_corrigida}:{minuto_corrigido} a.m.')
      elif hora_digitada >= 10 and hora_digitada < 12:
        if minuto_digitado < 10:
          print(f'Formato 12 horas => São: {hora_convertida}:{minuto_corrigido}a.m.')
      elif hora_digitada >= 10 and hora_digitada < 12:
        if minuto_digitado >= 10:
          print(f'Formato 12 horas => São: {hora_convertida}:{minuto_digitado}a.m.')
      elif hora_digitada >= 12 and minuto_digitado < 10:
        print(f'Formato 12 horas => São: {hora_convertida}:{minuto_corrigido}p.m.')
      elif hora_digitada >= 12 and minuto_digitado >= 10:
        print(f'Formato 12 horas => São: {hora_convertida}:{minuto_digitado}p.m.')

      print('\n')

    else: #todo o código para horas válidas está dentro do if dessa linha, ele só entra aqui se o formato digitado for inválido!
      print("\nFormato da hora digitada inválido. Por favor tente novamente!\n")
  
  elif opção_de_entrada == '2': #Condição para sair do programa;
    print('\nObrigado por usar o serviço!') #mensagem a ser apresentada ao usuário;
    break #Comando de saída do laço de repetição;

  else: #condição para quando o usuário digitar algo errado;
    print('\nOperação inválida. Por gentileza, tente novamente!\n') #Mensagem a ser impresso caso o usuário digitar uma operação inválida;

'''
GUIA DO CÓDIGO:
hora_digitada => corresponde a hora digitada pelo usuário;
hora_corrigida => corresponde a hora digitada pelo usuário, mas que foi acrescentado zero a esquerda por ser menor que 10;
minuto_digitado => corresponde ao minuto digitado pelo usuário;
minuto_corrigido => corresponde ao minuto digitado pelo usuário, mas que foi acrescentado zero a esquerda por ser menor que 10;
hora_convertida => corresponde a hora digitada pelo usuário, mas que foi convertida para o formato de 12 horas para ser impresso;
str(<variável>).zfill(<quantidade de digitos incluindo o zero>) => corresponde a função que acrescenta zero a esquerda do numero digitado;
'''