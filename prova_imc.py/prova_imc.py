# autor: joão gabriel
# projeto: condicionais 

# definbição das variaveis 
nome = input('digite seu nome: ')
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f'seu imc {imc:.2f} esta abixo da tabela ')
elif imc <= 24.9:
    print(f'seu imc {imc:.2f} esta agradavel ')
elif imc <= 29.9:
    print(f'seu imc {imc:.2f} voce esta acima do peso indicado ')
elif imc <= 34.9:
    print(f'seu imc {imc:.2f} voce se encontra em obsidade gral 1')
elif imc <= 39.9:
    print(f'seu imc {imc:.2f} voce se encontra em obsidade gral 2')
else:
    print(f'seu imc {imc:.2f} voce se encontra em obsidade gral 3 Procure um medico')