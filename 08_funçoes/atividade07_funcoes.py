nome = input('digite o seu nome:')
peso = float(input('digite seu peso:'))
altura = float(input('digite sua altura:'))
def calcular(peso,altura):
    imc = peso/(altura*altura)
    if imc <=18.5:
        print(' abaixo do peso! ')
    else:
        print(' peso normal! ')
calcular (peso,altura)