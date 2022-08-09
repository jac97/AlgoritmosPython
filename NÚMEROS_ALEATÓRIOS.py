import random #importei o modulo random para poder gerar números aleatórios;

lista = list(range(-5000, 5001)) #comando para gerar números aleatórios num intervalo de -5000 e 5000;

lista_gerada = random.choices(lista, k=100) #usei a função random.choices do modulo random para gerar uma lista aleatória com 100 elementos dentro da lista com intervalo de -5000 a 5000;

#tamanho = len(lista_gerada) #essa linha aqui calcula o tamanho da lista gerada para saber se está correto mesmo;

#criação de listas vazias para receberem os respectivos números correspondentes a exigência da questão;
lista_pares = []
lista_impares = []
lista_positivos = []
lista_negativos = []
lista_multiplos_7 = []

for chave in lista_gerada: #percorrimento da lista gerada aleatóriamente com 100 elementos;

    if chave % 2== 0: #verificação de número pares;
        lista_pares.append(chave) #adição dos números pares a sua lista pares;

    if (chave % 2 != 0): #verificação de números ímpares;
        lista_impares.append(chave) #adição de números ímpares a lista ímpares

    if(chave >= 0): #verificação números positivos maiores que zero;
        lista_positivos.append(chave) #adição de números positivos maiores que zero a lista positivos;

    if (chave < 0): #verificação de números negativos;
        lista_negativos.append(chave) #adição de números negativos a lista negativos;

    elif(chave % 7 == 0): #verificação de múltiplos de sete;
        lista_multiplos_7.append(chave) #adição de números múltiplos de sete a lista multiplos_7;

#comando de saída
print(f'CONFIRA ABAIXO O RESULTADO DOS CALCULOS:\n')
#print('Lista gerada: ', lista) #aqui eu posso imprimir a lista gerada de 100 elementos se eu quiser que o usuário veja a essa lista cada vez que ela for gerada;
#print('Tamanho da lista gerada: ', tamanho) #essa linha do código permite ver o tamanho da lista gerada para poder ter certeza que são 100 elementos;
print('\nLista de números pares: ', lista_pares) #lista dos números pares;
print('\nLista de números ímpares: ', lista_impares) #lista dos números ímpares;
print('\nLista de números positivos: ', lista_positivos) #lista dos números positivos maiores que zero;
print('\nLista de números negativos: ', lista_negativos) #lista dos números negativos;
print('\nLista de números múltiplos de 7: ', lista_multiplos_7) #lista dos números múltiplos de 7;

'''
GUIA DO CÓDIGO:
import.random => serve para importar o modulo random que permite a geração de números e até lista de números aleatórios;
random.choices(<variável>, k=<tamanho desejado>) => serve para escolher 100 elementos aleatórios e colocar eles na lista criada, no intervalo solicitado;
list(range(a,b)) => serve para gerar números aleatórios em um intervalo de a até b;
len(<variável>) => serve para calcular o tamanho de uma variável, nesse caso uma lista;
<variável> = [] => serve para criar uma lista vazia;
<variável>.append(chave) => serve para adicionar uma variável a uma lista nesse caso;
'''