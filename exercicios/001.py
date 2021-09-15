numero1=float(input('Escolha o primeiro número'))
numero2=float(input('Escolha o segundo número')) 
operacao=int(input('Escolha uma operacao: \n [1] Soma \n [2] Sutração \n [3] Multiplicação \n [4] Divisão'))
valor = 0 

if (operacao == 1):
  valor = numero1 + numero2
elif (operacao == 2):
  valor = numero1 - numero2
elif (operacao == 3):
  valor = numero1 * numero2
elif (operacao == 4):
  if (numero2 == 0):
    print("Não podemos fazer divisãão por 0")
  else:
    valor = numero1 / numero2
else:
  print("Valor inválido, tente outro número") 

print(' O valor da operação é:{}'.format(operacao))
print(' O resultado da operação é:{}'.format(valor)