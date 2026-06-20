# autor: joão gabriel
# projeto: condicionais 

# definição das variaveis
nome = input('digite seu nome: ')
temperatura = float(input('digite sua temperatura: '))
def calcular(temperatura):
    if temperatura >= 20:
        print('temperatura maior!')
    else:
        print('temperatura menor!')
calcular(temperatura)        