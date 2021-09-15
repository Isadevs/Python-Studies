nome=input('Qual o seu nome\n')
idade=int(input('Qual a sua Idade\n'))

#>29  >45 >59 >65

if (idade < 10):
    print('{} , você irá pagar R$30,00'.format(nome))

elif(idade >10) and (idade <=29):
    print('{} , você irá pagar R$60,00'.format(nome))

elif(idade > 29) and (idade <=45):
    print('{} , você irá pagar R$120,00'.format(nome))

elif(idade > 45) and (idade <=59):
    print('{} , você irá pagar R$150,00'.format(nome))

elif (idade > 59) and (idade <= 65):
    print('{} , você irá pagar R$250,00'.format(nome))

else:
    print('{} , você irá pagar R$400,00'.format(nome))
