#Abaixo está uma string que contém o menu que será apresentado usuário, ele só vai deixar de aparecer se o usuário escolher sair do programa;
menu = ''' \tMenu de Opções:
1 ----------------------------> Entrar com os dados para o calculo do IMC
2 ----------------------------> Sair do programa!
\nEscolha a operação que deseja realizar: '''

while True: #Comando do loop
  mensagem = input(menu) #impr ime o string "menu" logo no início do laço de repetição;

  if mensagem == '1': #Condição para calcular o IMC
    print('\n')
    #Entrada de dados por parte do usuário
    peso = float(input('Por favor, digite o seu peso (em kg): '))
    altura = float(input('Agora, digite sua altura (em metros) para prosseguir: '))

    imc = peso / (altura**2) #Código para calcular o Índice de Massa Corporal (IMC);

    if imc < 20: #se o IMC for menor que 20;
      faixa_de_risco = "Abaixo do peso" #a palavra "Abaixo do peso é atribuida ao variável faixa_de_peso caso o IMC for menor que 20";

    elif imc >= 20 and imc <= 25: #se o IMC for maior ou igual a 20 e menor ou igual que 25;
      faixa_de_risco = "Normal"

    elif imc >= 25 and imc <= 30: #se o IMC for maior ou igual a 25 e menor ou igual que 30;
      faixa_de_risco = "Excesso de peso"

    elif imc >= 30 and imc <= 35: #se o IMC for maior ou igual a 30 e menor ou igual que 35;
      faixa_de_risco = "Obesidade"

    else: #caso contrário o IMC for diferente de todas as opções acima, ou seja, estiver acima de 35;
      faixa_de_risco = "Obesidade Mórdida"

    #A tabela abaixo serve como guia para orientar o usuário a entender melhor como é feita a classificação da faixa de risco;
    print(f'\n\t\tDE ACORDO COM A TABELA DE FAIXA DE RISCO DO IMC\n')
    print('\t','+' * 68) #essa linha de código imprime até 68 vezes o caráter "+"
    print('\t |      IMC                                   Faixa de Risco        |')
    print('\t |                                                                  |')
    print('\t | Abaixo de 20 ----------------------------> Abaixo do peso        |')
    print('\t | Entre 20 e 25 (inclusive) ---------------> Normal                |')
    print('\t | Entre 25 e 30 (inclusive) ---------------> Excesso de peso       |')
    print('\t | Entre 30 e 35 (inclusive) ---------------> Obesidade             |')
    print('\t | Acima de 35 -----------------------------> Obesidade Mórbida     |')
    print('\t','+' * 68, '\n')

    print(f'O seu Índice de Massa Corporal (IMC) é igual a: {imc:.2f}') #imprime o resultado do calculo de IMC;
    print(f'O seu Índice de Massa Corporal te coloca na faixa de risco: {faixa_de_risco}.\n' ) #imprime a faixa de risco do usuário baseado no IMC calculado;

  elif mensagem == '2': #Condição para sair do programa;
    break #Comando de saída do laço de repetição;

  else:
    print('\nOperação inválida. Por favor, tente novamente!\n') #Mensagem a ser impresso caso o usuário digitar uma operação inválida;

print(f'\nAgradecemos a sua participação. Volte sempre que precisar!') #Mensagem de agradecimento impresso após o usuário escolher sair;