# autor: joão gbariel vieira silva 
# projeto: IMC input e f-string

# declaração de variaveis 
peso = float(input('digite o peso : '))
altura = float(input('digite a altura: '))

IMC = peso / (altura * altura)

# exibir os resultados 
print(f'o resultado do IMC e: {IMC:.2f}')