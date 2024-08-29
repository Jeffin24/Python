print('CONTAR PALAVRAS')
texto = input('Insira o texto a ser contado: ')
comprimento = int(input('Qual o tamanho das palavras: '))
lista_palavra = texto.split()
contador = 0
for palavra in lista_palavra:
    if len(palavra)==comprimento:
        contador += 1



print('A quantidade de palavras com o comprimento',comprimento,'é:',contador)