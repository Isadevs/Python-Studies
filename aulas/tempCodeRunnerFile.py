numeroInvalido = True

while(numeroInvalido != True):
  nota=int(input('Escreva a sua nota entre zero e dez: '))
  if nota < 0 or nota > 10:
    print('Nota inválida, digite um valor entre zero e dez')
  else:
    numeroInvalido = False

print("O numero que voce digitou é {}".format(nota))