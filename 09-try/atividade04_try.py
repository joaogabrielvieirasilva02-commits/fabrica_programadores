# Autor : joao gabriel
# Projeto : entendendo tratamento 
try:
    altura = float(input('digite sua altura:'))
    peso = float(input('digite seu peso:'))
except:
    print('ERRO')
#calcular o IMC 
def calcular(peso,altura):
    imc = peso/(altura**2)
    print(f'seu IMC e : {imc}')
    calcular (peso,altura)
