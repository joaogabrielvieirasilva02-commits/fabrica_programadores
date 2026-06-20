# autor: joão gbariel vieira silva 
# projeto: entrada com input

# declaração de variaveis 
valor1 = float(input('digite o primeiro valor : '))
valor2 = float(input('digite o segundo valor: '))
# funcão calcular - 4 operações basicas
def calcular (valor1,valor2):
    somar = valor1 + valor2
    subtrair = valor1 - valor2
    multiplicar = valor1 * valor2
    dividir = valor1 / valor2
    print(f'o resultado da soma e: {somar}')
    print(f'o resultado da subtração e: {subtrair}')
    print(f'o resultado da multiplicação e: {multiplicar}')
    print(f'o resultado da divisão e: {dividir}')

#chamada da função
calcular(valor1,valor2)