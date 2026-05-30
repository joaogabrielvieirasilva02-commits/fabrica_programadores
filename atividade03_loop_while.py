#autor joao gabriel vieira silva 
#Projeto loop_while

numero = int(input('digite o primeiro numero da taboada: '))
i = int(input('digite o inicio da taboada: '))
f = int(input('digite o inicio fim da taboada: '))

while i <= f:
    print(f'{numero} x {i} = {numero * i}')
    i = i + 1