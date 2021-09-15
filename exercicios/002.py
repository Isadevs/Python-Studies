#Calcular o valor do salario

#vendas : 2 , 21.20
#marketing: 3,  25
#producao: 4, 26
#administracao: 8, 30

departamento=int(input('Escolha um departamento:\n[2]Vendas\n[3]Marketing\n[4]Produção\n[8]Administração\n'))
hora_trabalho=float(input('Quantas horas você trabalhou este mês?'))
salario=0

if (departamento == 2):
    salario=hora_trabalho*21.20
elif(departamento == 3):
     salario=hora_trabalho*25
elif(departamento == 4):
    salario=hora_trabalho*26
elif(departamento==8):
    salario=hora_trabalho*30
else print('Departamento inesistente \n Escolha um departamento:\n[2]Vendas\n[3]Marketing\n[4]Produção\n[8]Administração\n ')

print ('O valor do seu salário é {}:'.format(salario))
     
