#Triangulo escaleno: a!=b!=c!=a
#triangulo isoceles: a=b!=c ou a!=b=c ou a=c
#triangulo equilatero: a=b=c

lado1=float(input('Qual primeiro lado do triângulo: '))
lado2=float(input('Qual segundo lado do triângulo: '))
lado3=float(input('Qual terceiro lado do triângulo: '))

if ((lado1==lado2) and (lado2==lado3) and (lado1==lado3)):
    print('Classificação: Triângulo Equilátero')

elif ((lado1!=lado2) and (lado2!=lado3) and (lado1!=lado3)):
    print('Classificação: Triângulo Escaleno')

elif ((lado1!=lado2) and (lado2!=lado3) and (lado1!=lado3) and (lado1==lado2) and (lado2==lado3) and (lado1==lado3)):
    print('Classificação: Triângulo Isósceles')
