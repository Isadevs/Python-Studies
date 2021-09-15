#Faça um programa em Python que recebe o valor do salário mínimo,
#o número de horas trabalhadas, o número de dependentes do
#funcionário e a quantidade de horas extras trabalhadas. Calcule e
#imprima o salário a receber do funcionário seguindo as regras abaixo:

# O valor da hora trabalhada é igual a 1/5 do salário mínimo;
# O salário do mês é igual ao número de horas trabalhadas vezes
#o valor da hora trabalhada;
# Para cada dependente acréscimo de R$ 43,00;
# Para cada hora extra trabalhada o cálculo do valor da hora
#trabalhada acrescida de 50%;
# O salário bruto é igual ao salário do mês mais os valores dos
#dependentes mais os valores da hora extras;
# O cálculo do valor do imposto de renda retido na fonte segue a
#tabela abaixo:

sal_min = float(input('Qual o valor do Salário Mínimo?\n'))
num_depen = int(input('Qual o número de dependentes?\n'))
num_hr_trab = float(input('Qual o número de horas trabalhadas\n'))
hr_extra = float(input('Quantas horas extras você fez?\n'))
hr_trab = 0
irrf = 0

print(('--------------------------------------'))
print(('        FOLHA   DE  PAGAMENTO'))
print(('--------------------------------------'))

hr_trab = (0.2*sal_min)
print('Débito - Horas trabalhadas: {}h'.format(hr_trab))

sal_mes = (hr_trab*num_hr_trab)
print('Débito - Salário do Mês: R$ {}'.format(sal_mes))

sal_depen = (num_depen*43)
print('Dépito - Dependente: R$ {}'.format(sal_depen))

sal_hr_extra = (hr_extra*hr_trab)*0.5
print('Débito - Hora extra: R$ {}'.format(sal_hr_extra))

sal_bruto = (sal_mes+sal_depen+sal_hr_extra)
print('Salário bruto:R$ {}'.format(sal_bruto))

if (sal_bruto < 2000):
   irrf = sal_bruto*0
   print('\nVocê está isento de imposto')

else:
    if (sal_bruto == 2000) or (sal_bruto <= 5000):
        irrf = sal_bruto*0.1

    elif (sal_bruto > 5000):
        irrf = sal_bruto*0.2 
        print('\nVocê deverá pagar: R${:.2f} de imposto'.format(irrf))

sal_liq = (sal_bruto - irrf)

if (sal_liq < 3500):
    sal_liq+250

elif (sal_liq >=3500):
    sal_liq+100
print(('--------------------------------------'))
print(('Salário Líquido:R$ {}'.format(sal_liq)))


