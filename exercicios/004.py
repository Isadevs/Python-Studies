altura=float(input('Qual a sua Altura\n\n'))
sexo=input('Qual o seu sexo? F/M\n')

if (sexo=='F' or'f'):
    peso_ideal=(62.1*altura)-44.7
    print('Seu Peso Ideal é:{}'.format(peso_ideal))

elif(sexo=='M' or 'm'):
    peso_ideal=(72.7*altura)-58
    print('Seu Peso Ideal é:{}'.format(peso_ideal))
else:
    print('Sexo inválido, tente F/M')